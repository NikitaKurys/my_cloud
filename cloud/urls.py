from django.urls import path, include

from cloud.views import user_views, file_views

app_name = 'cloud'

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('registr/', user_views.RegUserView.as_view()),
    path('files/', file_views.FileView.as_view()),
    path('link/', file_views.get_link),
    path('link/<str:link>/', file_views.get_file),
    path('detail_users_list/', user_views.get_detail_user_list),
]
