from abc import abstractmethod, ABC

from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication

from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication


class CustomizeTokenObtainPairSerializer(TokenObtainPairSerializer):
    # @abstractmethod
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # TODO:

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

    # def validate(self, attrs):
    #     authenticate_kwargs = {
    #         self.username_field: attrs[self.username_field],
    #         'password': attrs['password'],
    #     }
    #     try:
    #         authenticate_kwargs['request'] = self.context['request']
    #     except KeyError:
    #         pass
    #     user = authenticate(**authenticate_kwargs)
    #     if user is not None:
    #         return self.get_token(user)
    #     else:
    #         return Response(status=status.HTTP_401_UNAUTHORIZED)


class CustomizeTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomizeTokenObtainPairSerializer


class BlackListToken(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        pass

    def post(self, request):
        token = RefreshToken(request.data.get('refresh'))
        token.blacklist()
        return Response('Success', status=status.HTTP_200_OK)
