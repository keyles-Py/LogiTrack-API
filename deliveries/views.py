from django.shortcuts import render
from rest_framework import viewsets
from .models import Delivery
from .serializers import DeliverySerializer

# Create your views here.
class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
