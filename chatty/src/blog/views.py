from django.contrib.auth.models import User
from rest_framework import viewsets, status
from django.db.models import Q, Count
from blog.models import Category, Article, CustomUser
from blog.serializers import CategorySerializer, ArticleSerializer, UserSerializer
from rest_framework.response import Response
from django.db import transaction, IntegrityError
from rest_framework.views import APIView

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()

class User(APIView):
    serializer_class = UserSerializer

    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    @transaction.atomic()
    def create(self, request, *args, **kwargs):
        try:
            test = Article.objects.annotate(Count('title'))
            testSerializer = ArticleSerializer(test)
            serializer = ArticleSerializer(data=request.data)
            if serializer.is_valid(raise_exception=ValueError):
                # article = serializer.create(validated_data=serializer.data)
                category = Category.objects.create(name='minhle', description='test')
                article = Article.objects.create(title='test title', content='123')
                article.categories.add(category)

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.error_messages,
                            status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError as e:
            transaction.set_rollback(True)
            return Response(serializer.error_messages,
                            status=status.HTTP_400_BAD_REQUEST)
