import os.path

from rest_framework import serializers
from django.core import files

from cloud.utils import get_download_link
from cloud.validators import file_validator
from .models import User, File


class RegUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField()

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'password', 'password2']

    def save(self):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name']
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({
                password: 'password does not match',
            })

        user.set_password(password)

        user.save()

        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_staff']


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = ['file', 'comment', ]

    def create(self, **kwargs):

        file = files.File(self.validated_data['file'])
        user = User.objects.filter(id=kwargs['user_id']).first()
        data = {
            'user': user,
            'file_name': file.name,
            'path_to_the_file': f'media/files/{user}/{file.name}',
            'size': file.size,
            'comment': self.validated_data['comment'],
            'download_link': get_download_link(),
            'file': self.validated_data['file'],
        }
        try:
            file_model = File.objects.create(**data)

            return file_model

        except Exception as err:
            error = {
                'message': ', '.join(err.args) if len(err.args) > 0 else 'Unknown Error'
            }

            raise serializers.ValidationError(error)

    def patch(self, **kwargs):

        validated_data = file_validator(self.initial_data)

        file = File.objects.filter(user_id=kwargs['user_id']).all().filter(id=validated_data['id']).first()
        if file:
            file.file_name = validated_data['file_name']
            file.comment = validated_data['comment']

            return file.save()


