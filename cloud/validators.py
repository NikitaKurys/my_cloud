from rest_framework import serializers


def file_validator(data):

    if 'file_name' not in data:
        raise serializers.ValidationError({
            'message': 'отсутствует имя файла',
        })

    if 'comment' not in data:
        raise serializers.ValidationError({
            'message': 'отсутсвует комментарий',
        })

    return data
