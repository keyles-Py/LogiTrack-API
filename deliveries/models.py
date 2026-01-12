from django.db import models
from django.contrib.auth.models import User
from vehicles.models import Vehicle
from django.core.exceptions import ValidationError

# Create your models here.
class Delivery(models.Model):
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2) # Mejor para dinero
    description = models.TextField()

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='deliveries')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='deliveries')
    
    def clean(self):
        if self.vehicle and self.vehicle.status == 'maintenance':
            raise ValidationError(f"The vehicle {self.vehicle.plate} in in maintenance")
        
    def __str__(self):
        return f"Entrega {self.id} - {self.destination}"
