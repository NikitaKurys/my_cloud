from django.urls import path

from cloud.views.auth_views import login_view, logout_view, get_csrf_token, me_view
from cloud.views.file_views import FileView, get_link, get_file
from cloud.views.user_views import delete_user, RegUserView, get_detail_user_list

app_name = 'cloud'

urlpatterns = [
    path('auth/login/', login_view),
    path('auth/logout/', logout_view),
    path('auth/get_csrf/', get_csrf_token),
    path('auth/me/', me_view),
    path('registr/', RegUserView.as_view()),
    path('files/', FileView.as_view()),
    path('link/', get_link),
    path('delete_user/<int:user_id>/', delete_user),
    path('link/<str:link>/', get_file),
    path('detail_users_list/', get_detail_user_list),
]
