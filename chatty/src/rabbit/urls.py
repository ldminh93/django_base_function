from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from rabbit.views import index, login_view, logout_view, signup

# urlpatterns = patterns('',
#     # Examples:
#     path(r'^$', 'ribbit_app.views.index'), # root
#     path(r'^login$', 'ribbit_app.views.login_view'), # login
#     path(r'^logout$', 'ribbit_app.views.logout_view'), # logout
#     path(r'^signup$', 'ribbit_app.views.signup'), # signup
# )
urlpatterns = [
    path(r'', index, name='home'),
    path(r'login/', login_view, name='login'),
    path(r'logout/', logout_view, name='logout'),
    path(r'signup/', signup, name='signup'),
]