from rest_framework import serializers
from .models import Delivery
from vehicles.serializers import VehicleSerializer

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'
