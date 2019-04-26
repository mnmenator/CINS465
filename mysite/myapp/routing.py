from django.conf.urls import url

from . import consumers

WEBSOCKET_URLPATTERNS = [
    url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
]
