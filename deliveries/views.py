from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .services import DeliveryService
from .models import Delivery
from .serializers import DeliverySerializer

# Create your views here.
class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.select_related('vehicle').all()
    serializer_class = DeliverySerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            delivery = DeliveryService.create_delivery(
                user=request.user,
                vehicle=serializer.validated_data['vehicle'],
                origin=serializer.validated_data['origin'],
                destination=serializer.validated_data['destination'],
                price=serializer.validated_data['price'],
                description=serializer.validated_data['description']
            )
            response_serializer = self.get_serializer(delivery)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)