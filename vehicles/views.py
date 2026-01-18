from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Vehicle
from .serializers import VehicleSerializer

# Create your views here.
class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permissions_classes = [permissions.AllowAny]
        else:
            permissions_classes = [permissions.IsAdminUser]
        return [permission() for permission in permissions_classes]