from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from .views import index,settings,password,register

urlpatterns = [
    path(r'', index, name='home'),
    path(r'register/', register, name='register'),
    path(r'settings/', settings, name='settings'),
    path(r'settings/password/', password, name='password'),
    path(r'oauth/', include('social_django.urls', namespace='social')),  # <--

]