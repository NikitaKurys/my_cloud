from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.db import models

from cloud.utils import get_download_link


file_system = FileSystemStorage(location='user_storage')


class UserManager(BaseUserManager):
    def _create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError('No email specified')

        if not username:
            raise ValueError('No username specified')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **extra_fields,
        )

        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_user(self, email, username, password):
        return self._create_user(email, username, password)

    def create_superuser(self, email, username, password):
        return self._create_user(email, username, password, is_staff=True, is_superuser=True)


class File(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    file_name = models.CharField(max_length=70, verbose_name='название файла')
    path_to_the_file = models.CharField(unique=True, max_length=50, verbose_name='путь к файлу')
    size = models.IntegerField(null=True, verbose_name='размер файла')
    upload_date = models.DateField(auto_now_add=True, null=True, verbose_name='дата загрузки')
    last_download_date = models.DateField(null=True, verbose_name='дата скачивания')
    comment = models.TextField(max_length=100, null=True, verbose_name='комментарии')
    download_link = models.CharField(null=True, max_length=50, default=get_download_link, verbose_name='ссылка для скачивания')
    file = models.FileField(storage=file_system, blank=True)

    class Meta:
        verbose_name = 'Файлы'
        verbose_name_plural = verbose_name
