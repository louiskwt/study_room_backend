from django.shortcuts import render
from rest_framework import generics, status
from .serializers import CreateRoomSerializer, RoomSerializer
from .models import Room
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class CreateRoomView(APIView):
    serializer_class = CreateRoomSerializer
    renderer_classes = [JSONRenderer]

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            guest_can_pause = serializer.data.get('guest_can_pause')
            votes_to_skip = serializer.data.get('votes_to_skip')
            host = self.request.session.session_key
            queryset = Room.objects.filter(host=host)
            if queryset.exists():
                room = queryset[0]
                room.guest_can_pause = guest_can_pause
                room.votes_to_skip = votes_to_skip
                room.save(update_fields=['guest_can_pause', 'votes_to_skip'])
                print(RoomSerializer(room).data)
              
                return Response({"data": RoomSerializer(room).data}, status=status.HTTP_200_OK)
            else:
                room = Room(host=host, guest_can_pause=guest_can_pause, votes_to_skip=votes_to_skip)
                room.save()
                # content = {'data': RoomSerializer(room).data}
                print(RoomSerializer(room).data)
                return Response({"data": RoomSerializer(room).data} , status=status.HTTP_201_CREATED)
            
        return Response({'Bad Request': "invalid data"}, status=status.HTTP_400_BAD_REQUEST)