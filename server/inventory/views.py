from rest_framework import viewsets
from .models import Inventory, InventorySerialNumber
from .serializers import InventorySerializer, InventorySerialNumberSerializer

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

class InventorySerialNumberViewSet(viewsets.ModelViewSet):
    queryset = InventorySerialNumber.objects.all()
    serializer_class = InventorySerialNumberSerializer
