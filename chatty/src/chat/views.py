from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication

from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Message
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import authentication, permissions, viewsets


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

    def validate(self, attrs):
        authenticate_kwargs = {
            self.username_field: attrs[self.username_field],
            'password': attrs['password'],
        }
        try:
            authenticate_kwargs['request'] = self.context['request']
        except KeyError:
            pass
        self.user = authenticate(**authenticate_kwargs)
        return {}


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


def index(request):
    return render(request, 'chat/index.html')


def signin(request):
    if request.user.is_authenticated:
        return redirect('')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request=request, user=user)
            return render(request, 'chat/index.html')
    return render(request, 'registration/login.html')

# def logout(request):


def room(request, room_name):
    username = request.GET.get('username', 'Anonymous')
    messages = Message.objects.filter(room=room_name).order_by('-id')[0:25]

    return render(request, 'chat/room.html',
                  {'room_name': room_name, 'username': username, 'messages': reversed(messages)})


class Detail(APIView):
    pass


class RefreshToken(APIView):
    # query_set = Message.objects.all()
    # serializer_class = ArticleSerializer

    query_set = Message.objects.all()
    # lookup_field = 'user_id'
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = {
            'result': 123
        }
        return Response(data=data)

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass

    def patch(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass


class MessageDetail(APIView):
    """
    A viewset that provides the standard actions
    """
    queryset = Message.objects.all()
    # serializer_class = UserSerializer
    lookup_field = 'username'

    @action(detail=True)
    def get(self, request, pk=None):
        """
        Returns a list of all the group names that the given
        user belongs to.
        """
        message = self.get_object()
        groups = message.groups.all()
        return Response([group.name for group in groups])