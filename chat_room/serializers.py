from rest_framework import serializers
from django.contrib.auth.models import User
from chat_room.models import Room, Chat


class UserSerializer(serializers.ModelSerializer):
    # User Serializer
    class Meta:
        model = User
        fields = ('id', 'username')


class RoomSerializer(serializers.ModelSerializer):
    # Chat Room serializer
    creator = UserSerializer()
    invited = UserSerializer(many=True)

    class Meta:
        model = Room
        fields = ('creator', 'invited', 'date')


class ChatSerializer(serializers.ModelSerializer):
    # Chat Serializer
    user = UserSerializer()

    class Meta:
        model = Chat
        fields = ("user", "text", "date")


class ChatPostSerializer(serializers.ModelSerializer):
    # Chat Serializer
    class Meta:
        model = Chat
        fields = ("room", "text",)
