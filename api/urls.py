from django.urls import path
from .views import RoomView, CreateRoomView

urlpatterns = [
    path('room', RoomView.as_view(), name='home'),
    path('create-room', CreateRoomView.as_view(), name='create-room'),
]