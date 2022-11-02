from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),
    path('blog/', include('blog.urls')),
    # path('search/', include('search.urls')),
    path('auth/', include('auth.urls')),
    path('home/', include('home.urls')),
    path('blockchain/', include('blockchain.urls')),
    path('stream/', include('stream.urls')),
    # path('rabbit/', include('rabbit.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
