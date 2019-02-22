from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from chat_room.serializers import RoomSerializer
from chat_room.models import Room


class Rooms(APIView):
    # Chat Rooms
    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response({'data': serializer.data})

