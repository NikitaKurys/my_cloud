# Generated by Django 4.1.6 on 2023-03-11 18:59

import cloud.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('file_name', models.CharField(max_length=70, verbose_name='название файла')),
                ('path_to_the_file', models.CharField(max_length=50, unique=True, verbose_name='путь к файлу')),
                ('size', models.IntegerField(null=True, verbose_name='размер файла')),
                ('upload_date', models.DateField(auto_now_add=True, null=True, verbose_name='дата загрузки')),
                ('last_download_date', models.DateField(null=True, verbose_name='дата скачивания')),
                ('comment', models.TextField(max_length=100, null=True, verbose_name='комментарии')),
                ('download_link', models.CharField(default=cloud.utils.get_download_link, max_length=50, null=True, verbose_name='ссылка для скачивания')),
                ('file', models.FileField(blank=True, upload_to=cloud.utils.get_file_path)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'Файлы',
                'verbose_name_plural': 'Файлы',
            },
        ),
    ]
