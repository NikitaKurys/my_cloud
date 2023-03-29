import os
import random
import string


def get_file_path(instance, filename):
    """Путь к файлам пользователей"""

    path_file = os.path.join('files', str(instance.user.username), filename)
    return path_file


def get_download_link():
    """Ссылка для скачивания файла"""

    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(25))
    return rand_string
