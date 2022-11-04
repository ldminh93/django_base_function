import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Message


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
    
    async def disconnect(self, close_code):
        # Leave room
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    # Receive message from web socket
    async def receive(self, text_data):
        data = json.loads(text_data)
        action = data['action']
        message = data['message']
        username = data['username']
        room = data['room']
        if action == 'send':
            await self.save_message(username, room, message)

            # Send message to room group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'action': action,
                    'message': message,
                    'username': username
                }
            )
        elif action == 'typing':
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'typing_signal',
                    'action': action,
                    'username': username
                }
            )
        elif action == 'un_typing':
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'typing_signal',
                    'action': action,
                    'username': username
                }
            )
    async def typing_signal(self, event):
        action = event['action']
        username = event['username']
        await self.send(text_data=json.dumps({
            'action': action,
            'username': username
        }))

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        action = event['action']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'action': action,
            'message': message,
            'username': username
        }))

    @sync_to_async
    def save_message(self, username, room, message):
        Message.objects.create(username=username, room=room, content=message)