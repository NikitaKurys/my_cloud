from datetime import date

from django.http import FileResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from cloud.models import File, file_system
from cloud.serializers import FileSerializer


class FileView(APIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self, user_id=None):

        if self.request.user.is_staff and user_id:
            return File.objects.filter(user=user_id).all()

        return File.objects.filter(user=self.request.user.id).all()

    def get(self, request):

        if 'id' not in request.query_params:
            user_id = None

            if 'user_id' in request.query_params:
                user_id = request.query_params['user_id']

            files = self.get_queryset(user_id).values('id', 'user__username', 'size', 'file_name', 'upload_date',
                                                      'last_download_date', 'comment')
            return Response(files)

        file = self.get_queryset().filter(id=request.query_params['id']).first()

        if file:
            file.last_download_date = date.today()
            file.save()
            return FileResponse(file.file, status.HTTP_200_OK, as_attachment=True)

        data = {
            'message': 'The file not found',
        }

        return Response(data, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = FileSerializer(data=request.data)

        data = {}

        if serializer.is_valid():
            serializer.create(user_id=request.user.id, file=request.FILES['file'])

            data = self.get_queryset().values('id', 'user__username', 'size', 'file_name', 'upload_date',
                                              'last_download_date', 'comment')

            return Response(data, status=status.HTTP_200_OK)

        data = serializer.errors

        return Response(data)

    def patch(self, request):
        serializer = FileSerializer(data=request.data)

        data = {}

        if serializer.is_valid():
            user = request.user

            serializer.patch(
                user=user,
            )

            if 'user_storage_id' in request.query_params and user.is_staff:
                data = self.get_queryset(
                    user_id=request.query_params['user_storage_id']
                ).values(
                    'id',
                    'user__username',
                    'size',
                    'file_name',
                    'upload_date',
                    'last_download_date',
                    'comment',
                )
            else:
                data = self.get_queryset().values(
                    'id',
                    'user__username',
                    'size',
                    'file_name',
                    'upload_date',
                    'last_download_date',
                    'comment'
                )

            return Response(data)

        data = serializer.errors

        return Response(data)

    def delete(self, request):
        if request.user.is_staff:
            deleted_file = File.objects.filter(
                id=int(request.query_params['id'])
            ).first()
        else:
            deleted_file = File.objects.filter(
                user_id=request.user.id
            ).all().filter(
                id=int(request.query_params['id'])
            ).first()

        if deleted_file:
            file_system.delete(deleted_file.path_to_the_file)

            deleted_file.delete()

            user = request.user

            if 'user_storage_id' in request.query_params and user.is_staff:
                data = self.get_queryset(
                    user_id=request.query_params['user_storage_id']
                ).values(
                    'id',
                    'user__username',
                    'size', 'file_name',
                    'upload_date', 'last_download_date',
                    'comment',
                )
            else:
                data = self.get_queryset().values(
                    'id',
                    'user__username',
                    'size', 'file_name',
                    'upload_date',
                    'last_download_date',
                    'comment',
                )

            return Response(data, status.HTTP_200_OK)

        data = {
            'message': 'The file not found',
        }

        return Response(data, status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_link(request):
    user_id = request.user.id
    file_id = request.query_params['file_id']

    if request.user.is_staff:
        file = File.objects.filter(id=file_id).first()
    else:
        file = File.objects.filter(user_id=user_id).filter(id=file_id).first()

    if file:
        data = {
            'link': file.download_link,
        }

        return Response(data, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_file(request, link):
    file = File.objects.filter(download_link=link).first()

    if file:
        file.last_download_date = date.today()
        file.save()

        return FileResponse(file.file, status.HTTP_200_OK, as_attachment=True, filename=file.file_name)

    return Response(status=status.HTTP_404_NOT_FOUND)
