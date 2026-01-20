from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Vehicle
from .serializers import VehicleSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

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
    
    @method_decorator(cache_page(60*15))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)