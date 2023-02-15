from django.contrib import admin
from django.contrib.admin.models import LogEntry

from .models import Profile, File, UserLog


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    autocomplete_fields = ('user',)
    search_fields = ('user__username',)
    list_display = ('user', 'avatar')
    list_per_page = 10


@admin.register(File)
class ProfileAdmin(admin.ModelAdmin):
    search_fields = ('user__username',)
    list_display = ('user', 'file_name', 'path_to_the_file',
                    'size', 'upload_date', 'last_download_date',
                    'comment', 'download_link', 'file')
    list_filter = ('user', 'file_name',)
    list_per_page = 10


@admin.register(UserLog)
class UserLogAdmin(admin.ModelAdmin):
    search_fields = ('username',)
    list_display = ('username', 'ipaddress', 'browser', 'os', 'action', 'action_time')
    list_filter = ('action',)
    list_per_page = 15

    def has_add_permission(self, request):
        return False


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['object_repr', 'object_id', 'action_flag', 'user', 'change_message']
    list_per_page = 12
