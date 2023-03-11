from django.contrib import admin
from django.contrib.admin.models import LogEntry

from .models import File


@admin.register(File)
class ProfileAdmin(admin.ModelAdmin):
    search_fields = ('user__username',)
    list_display = ('user', 'file_name', 'path_to_the_file',
                    'size', 'upload_date', 'last_download_date',
                    'comment', 'download_link', 'file')
    list_filter = ('user', 'file_name',)
    list_per_page = 10


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['object_repr', 'object_id', 'action_flag', 'user', 'change_message']
    list_per_page = 12
