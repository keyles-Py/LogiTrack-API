from django.core.exceptions import ValidationError
from .models import Delivery
from vehicles.models import Vehicle
from .tasks import notify_delivery_creation

class DeliveryService:
    @staticmethod
    def create_delivery(user, vehicle, origin, destination, price, description):
        if vehicle.status == 'maintenance':
            raise ValidationError(
                f"El vehículo {vehicle.plate} no está disponible por mantenimiento"
            )
        delivery = Delivery.objects.create(
            user=user,
            vehicle=vehicle,
            origin=origin,
            destination=destination,
            price=price,
            description=description
        )
        notify_delivery_creation.delay(delivery.id)
        return delivery