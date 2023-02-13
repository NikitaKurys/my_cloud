from datetime import date

from django.http import FileResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from cloud.serializers import UserSerializer, FileSerializer
from .models import User, File


class UserView(CreateAPIView):
    queryset = User.objects.all()

    serializer_class = UserSerializer

    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        data = {}

        if serializer.is_valid():
            serializer.save()

            data['response'] = True

            return Response(data, status=status.HTTP_200_OK)

        else:
            data = serializer.errors

            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class FileView(APIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return File.objects.all()

        return File.objects.filter(user=self.request.user.id).all()

    def get(self, request):

        if 'id' not in request.query_params:
            files = self.get_queryset().values('id', 'size', 'upload_date', 'last_download_date', 'comment')
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

            data = {
                'message': 'The file has been added to the storage',
            }

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

            data = {
                'message': 'The file has been updated in the storage'
            }

            return Response(data)

        data = serializer.errors

        return Response(data)

    def delete(self, request):
        deleted_file = File.objects.filter(user_id=request.user.id).all().filter(
            id=int(request.query_params['id'])).first()

        if deleted_file:
            deleted_file.delete()

            return Response(status.HTTP_200_OK)

        data = {
            'message': 'The file not found',
        }

        return Response(data, status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_link(request):
    user_id = request.user.id
    file_id = request.data['file_id']

    file = File.objects.filter(user_id=user_id).filter(id=file_id).first()

    if file:
        data = {
            'link': file.public_download_id,
        }

        return Response(data, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_file(request, link):
    file = File.objects.filter(public_download_id=link).first()

    if file:
        file.last_download_date = date.today()
        file.save()

        return FileResponse(file.file, status.HTTP_200_OK, as_attachment=True, filename=file.native_file_name)

    return Response(status=status.HTTP_404_NOT_FOUND)
