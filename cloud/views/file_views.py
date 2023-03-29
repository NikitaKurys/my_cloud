from datetime import date

from django.http import FileResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from cloud.models import File
from cloud.serializers import FileSerializer


class FileView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FileSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return File.objects.all()

        return File.objects.filter(user=self.request.user.id).all()

    def get(self, request):

        if 'id' not in request.query_params:
            files = self.get_queryset().values('id', 'size', 'upload_date',
                                               'last_download_date', 'comment', 'file', 'file_name')
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

            data = self.get_queryset().values('id', 'user__username', 'size', 'path_to_the_file', 'upload_date',
                                              'last_download_date', 'comment', 'file_name')

            return Response(data, status=status.HTTP_200_OK)

        data = serializer.errors

        return Response(data)

    def patch(self, request):
        serializer = FileSerializer(data=request.data)

        data = {}

        if serializer.is_valid():
            serializer.patch(
                user_id=request.user.id,
            )

            data = self.get_queryset().values('id', 'user__username', 'size', 'file_name', 'upload_date',
                                              'last_download_date', 'comment')

            return Response(data)

        data = serializer.errors

        return Response(data)

    def delete(self, request):
        if request.user.is_staff:
            deleted_file = File.objects.filter(id=int(request.query_params['id'])).first()
        else:
            deleted_file = File.objects.filter(user_id=request.user.id).all().filter(
                id=int(request.query_params['id'])).first()

        if deleted_file:
            deleted_file.delete()

            data = self.get_queryset().values('id', 'user__username', 'size', 'file_name', 'upload_date',
                                              'last_download_date', 'comment')

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