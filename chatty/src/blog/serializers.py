from django.contrib.auth.models import User
import django.contrib.auth.password_validation as validators
from django.core.exceptions import ValidationError
from rest_framework import serializers

from blog.models import Article, Category, CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'password', 'gender', 'username', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_username(self, username):
        if len(username) < 6 or len(username) > 15:
            raise ValidationError('Username must be between 6 and 15 characters long')
        return username

    def validate_password(self, password):
        try:
            validators.validate_password(password)
        except ValidationError as exc:
            raise serializers.ValidationError(str(exc))
        return password

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])

        user.is_active = False
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        if 'password' in validated_data:
            user.set_password(validated_data['password'])
            user.save()
        return user

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    categories = CategorySerializer()

    class Meta:
        model = Article
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('author')
        category = validated_data.pop('categories')
        UserSerializer.create(UserSerializer(), validated_data=user_data)
        CategorySerializer.create(CategorySerializer(), validated_data=category)

        return
