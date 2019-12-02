from channels.consumer import SyncConsumer
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from time import sleep
from random import randint
import json

from channels.layers import get_channel_layer
channel_layer = get_channel_layer()


class BackgroundTask(SyncConsumer):
    def random_values(self, event):
        while True:
            r = randint(0, 100)
            async_to_sync(channel_layer.group_send)('group_random', {
                "type": "random_message",
                "value": r
            })
            # print(r)
            sleep(1)


class RandomConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = 'random'
        self.room_group_name = 'group_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        # print('connected')
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        value = text_data_json['value']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'random_message',
                'value': value
            }
        )

    # Receive message from room group
    def random_message(self, event):
        value = event['value']
        # print('sending', value)
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'value': value
        }))