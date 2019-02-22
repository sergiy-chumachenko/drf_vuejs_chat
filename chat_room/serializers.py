from rest_framework import serializers
from django.contrib.auth.models import User
from chat_room.models import Room


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
