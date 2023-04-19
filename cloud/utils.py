import random
import string


def get_download_link():
    """Ссылка для скачивания файла"""

    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(25))
    return rand_string


def get_ext(file_name):
    return file_name.split('.')[-1]


def generate_storage_file_name(file_name):
    ext = f".{get_ext(file_name)}"
    from cloud.models import file_system
    result = file_system.get_alternative_name('cloud', ext)
    return result
