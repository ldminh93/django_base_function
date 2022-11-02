from django.db import models
from django.contrib.auth.models import (
    User,
    AbstractUser,
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
)


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return f'{self.name}'


ARTICLE_TYPES = [
    ('UN', 'Unspecified'),
    ('TU', 'Tutorial'),
    ('RS', 'Research'),
    ('RW', 'Review'),
]
GENDER = [
    ('M', 'Male'),
    ('F', 'Female')
]


class ManageUser(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.is_staff = True
        user.save(using=self._db)

        return user


# class CustomUser(AbstractBaseUser):
#     email = models.EmailField(max_length=255, unique=True)
#     name = models.CharField(max_length=255)
#     is_active = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#
#     objects = ManageUser()
#     USERNAME_FIELD = 'email'


class CustomUser(AbstractUser):
    gender = models.CharField(max_length=128, choices=GENDER)


class EventManager(models.Manager):
    def event_type_count(self, event_type):
        return self.filter()


class Article(models.Model):
    title = models.CharField(max_length=256)
    author = models.ForeignKey(to=CustomUser, null=True, on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=ARTICLE_TYPES, default='UN')
    categories = models.ManyToManyField(to=Category, blank=True, related_name='categories')
    content = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)
    objects = EventManager()

    def type_to_string(self):
        if self.type == 'UN':
            return 'Unspecified'
        elif self.type == 'TU':
            return 'Tutorial'
        elif self.type == 'RS':
            return 'Research'
        elif self.type == 'RW':
            return 'Review'

    def __str__(self):
        return f'{self.author}: {self.title} ({self.created_datetime.date()})'
