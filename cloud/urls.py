from django.urls import path, include

from cloud import views

app_name = 'cloud'

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('registr/', views.RegistrUserView.as_view()),
    path('files/', views.FileView.as_view()),
    path('link/', views.get_link),
    path('link/<str:link>/', views.get_file),
    path('detail_users_list/', views.get_detail_user_list),
]
