from rest_framework import serializers
from .models import Delivery
from vehicles.serializers import VehicleSerializer

class DeliverySerializer(serializers.ModelSerializer):
    vehicle_details = VehicleSerializer(source='vehicle', read_only=True)
    class Meta:
        model = Delivery
        fields = [
            'id', 'origin', 'destination', 'price',
            'description', 'user', 'vehicle', 'vehicle_details'
        ]

    def validate(self, data):
        vehicle = data.get('vehicle')

        if vehicle and vehicle.status == 'maintenance':
            raise serializers.ValidationError({
                "vehicle": "No se puede asignar este vehiculo" 
            })
        
        return data