from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import File


@receiver(pre_delete, sender=File)
def file_model_delete(sender, instance, **kwargs):
    """"Удаление файла"""
    if instance.file.name:
        instance.file.delete(False)
