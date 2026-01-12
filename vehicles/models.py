from django.db import models

# Create your models here.

class Vehicle(models.Model):
    STATUS_CHOICES = [
        ('available', 'disponible'),
        ('on_route', 'en ruta'),
        ('maintenance', 'En mantenimiento'),
    ]

    plate = models.CharField(max_length=10, unique=True)
    model = models.CharField(max_length=50)
    vehicle_type = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')

    def __str__(self):
        return f'{self.plate} - {self.model}'