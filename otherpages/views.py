from .models import LiveStream, ToConnect
from .serializers import ToConnectSerializer
from rest_framework import generics

class ToConnectAPIView(generics.ListAPIView):
    queryset = ToConnect.objects.all()
    serializer_class = ToConnectSerializer
    