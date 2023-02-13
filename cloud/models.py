from django.contrib.auth.models import User
from django.db import models

from cloud.utils import get_image_path, get_file_path, get_download_link


class Profile(models.Model):
    """Профиль юзера"""

    GENDER = [
        ('0', 'Жен'),
        ('1', 'Муж'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='пользователь')
    gender = models.CharField(max_length=1, choices=GENDER, blank=True, verbose_name='пол')
    avatar = models.ImageField(upload_to=get_image_path, default='default/avatar.svg', verbose_name='аватар')

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username


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
    file = models.FileField(upload_to=get_file_path, blank=True)

    class Meta:
        verbose_name = 'Файлы'
        verbose_name_plural = verbose_name


class UserLog(models.Model):
    """Журнал посещений пользователя"""

    ACTIONS = [
        ('0', 'войти'),
        ('1', 'опубликовывать'),
        ('2', 'Ошибка входа')
    ]

    username = models.CharField(max_length=128, verbose_name='имя пользователя')
    ipaddress = models.GenericIPAddressField(verbose_name='IP-адрес :')
    browser = models.CharField(max_length=200, verbose_name='браузер')
    os = models.CharField(max_length=30, verbose_name='операционная система')
    action = models.CharField(max_length=1, choices=ACTIONS, verbose_name='действия')
    msg = models.CharField(max_length=100, verbose_name='данные')
    action_time = models.DateTimeField(auto_now_add=True, verbose_name='время')

    class Meta:
        verbose_name = 'Журнал посещений пользователя'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ipaddress
