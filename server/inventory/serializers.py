from rest_framework import serializers
from .models import Inventory, InventorySerialNumber

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'

class InventorySerialNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventorySerialNumber
        fields = '__all__'
