from django.contrib import admin

from blog.models import Category, Article, CustomUser


admin.site.register(Category)
admin.site.register(Article)
admin.site.register(CustomUser)