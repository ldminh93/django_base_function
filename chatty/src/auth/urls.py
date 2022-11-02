from django.urls import path, include
from rest_framework import routers

from .views import CustomizeTokenObtainPairView, BlackListToken
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView
urlpatterns = [

    path('login/', CustomizeTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/blacklist/', BlackListToken.as_view(), name='black_list'),
    path(r'oauth/', include('social_django.urls', namespace='social_auth')),
    # path('test/', RefreshToken.as_view(), name='test'),
    # path('test/<str:pk>/', MessageDetail.as_view(), name='message-detail')
    # path('test/', include(router.urls)),
    # path('', include(router.urls)),
]