import os
import random
import string


def get_image_path(instance, image_name):
    """Путь к аватаркам пользователей"""

    path_image = os.path.join('avatars', str(instance.user.username), image_name)
    return path_image


def get_file_path(instance, filename):
    """Путь к файлам пользователей"""

    path_file = os.path.join('files', str(instance.user.username), filename)
    return path_file


def get_download_link():
    """Ссылка для скачивания файла"""

    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(25))
    return f'https://{rand_string}'

