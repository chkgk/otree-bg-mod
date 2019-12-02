# channel routes for inclusion in a ChannelNameRouter
from .consumers import BackgroundTask, RandomConsumer
from django.conf.urls import url

channel_name_routes = {
    "backgroundworker": BackgroundTask,
}

websocket_routes = [
    url(r"^ws/random/group_random/$", RandomConsumer)
]