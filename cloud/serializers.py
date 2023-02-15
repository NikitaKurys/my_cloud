from rest_framework import serializers
from django.core import files

from cloud.utils import get_file_path, get_download_link
from cloud.validators import file_validator
from .models import User, File, Profile


class UserRegistrSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', ]

    def save(self):
        user = User(
            username=self.validated_data['username'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            password=self.validated_data['password'],
            email=self.validated_data['email'],
        )

        user.save()
        return user


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
            'path_to_the_file': get_file_path,
            'size': file.size,
            'comment': self.validated_data['comment'],
            'download_link': get_download_link,
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
