from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from chat_room.serializers import (RoomSerializer, ChatSerializer, ChatPostSerializer)
from chat_room.models import Room, Chat


class Rooms(APIView):
    # Chat Rooms
    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response({'data': serializer.data})


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
