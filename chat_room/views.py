from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from chat_room.serializers import (RoomSerializer, ChatSerializer, ChatPostSerializer, UserSerializer)
from chat_room.models import Room, Chat
from django.contrib.auth.models import User
from django.db.models import Q


class Rooms(APIView):
    # Chat Rooms
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        rooms = Room.objects.filter(Q(creator=request.user) | Q(invited=request.user)).distinct()
        serializer = RoomSerializer(rooms, many=True)
        return Response({'data': serializer.data})

    def post(self, request):
        Room.objects.create(creator=request.user)
        return Response(status=201)


class Dialog(APIView):
    # Dialog
    permission_classes = [permissions.IsAuthenticated, ]
    # permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        room = request.GET.get('room')
        chat = Chat.objects.filter(room=room)
        serializer = ChatSerializer(chat, many=True)
        return Response({'data': serializer.data})

    def post(self, request):
        # room = request.GET.get('room')
        dialog = ChatPostSerializer(data=request.data)
        if dialog.is_valid():
            dialog.save(user=request.user)
            return Response(status=201)
        else:
            return Response(status=400)


class AddUsersRoom(APIView):
    # Add User to the Chat Room
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        room = Room.objects.get(id=request.GET.get('room'))
        invited_users = room.get_invited_users()
        users = User.objects.exclude(Q(username=request.user) | Q(id__in=[user.id for user in invited_users]))
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        room = request.data.get('room')
        user_id = request.data.get('user')
        try:
            room = Room.objects.get(id=room)
            room.invited.add(user_id)
            room.save()
            return Response(status=201)
        except ValueError:
            return Response(status=400)
