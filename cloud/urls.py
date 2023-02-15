from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cloud import views

app_name = 'cloud'

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('registr/', views.UserRegistrView.as_view()),
    path('files/', views.FileView.as_view()),
    # path('link/', views.get_link),
    # path('link/<str:link>/', views.get_file),
]