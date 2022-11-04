
from django.urls import path, re_path

from . import consumers

websocket_urlpatterns = [
    path('ws/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
    # path('ws/test/', consumers.ChatConsumer.as_asgi()),
]
# websocket_urlpatterns = [
#    re_path('^ws/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
# ]

# websocket_urlpatters = [
#     path("ws/<str:room_name>/", consumers.ChatConsumer.as_asgi()),
# ]