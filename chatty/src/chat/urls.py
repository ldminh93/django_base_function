from django.urls import path, include
from rest_framework import routers
from . import views
from .views import RefreshToken, MyTokenObtainPairView, MessageDetail
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView
from . import consumers
urlpatterns = [
    path('home/', views.index, name='chat.home'),
    path('home/<str:room_name>/', views.room, name='room'),
    path('login/', views.signin, name='login'),
    path('logout/', views.signout, name='chat.signout'),
    # path("accounts/", include("django.contrib.auth.urls")),

]