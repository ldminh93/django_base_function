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
    path('home/', views.index, name='index'),
    path('home/<str:room_name>/', views.room, name='room'),


    # path('test/', RefreshToken.as_view(), name='test'),
    # path('test/<str:pk>/', MessageDetail.as_view(), name='message-detail')
    # path('test/', include(router.urls)),
    # path('', include(router.urls)),
]