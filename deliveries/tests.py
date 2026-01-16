from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Delivery
from vehicles.models import Vehicle

class DeliveryTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password123")

        self.client.login(username='testuser', password='password123')

        self.vehicle_ok = Vehicle.objects.create(
            plate="ABC-123", model="Tesla Semi", status="available"
        )
        self.vehicle_bad = Vehicle.objects.create(
            plate="BAD-666", model="Old Truck", status="maintenance"
        )
    def test_create_delivery_with_maintenance_vehicle_fails(self):
        url = '/api/deliveries/'
        data = {
            "origin": "Calle A",
            "destination": "Calle B",
            "price": "100.00",
            "description": "Carga pesada",
            "user": self.user.id,
            "vehicle": self.vehicle_bad.id
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("No se puede asignar", str(response.data))