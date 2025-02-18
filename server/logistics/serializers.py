from rest_framework import serializers
from .models import Address, Contact, Warehouse, Carrier, CarrierService

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'

class CarrierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrier
        fields = '__all__'

class CarrierServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarrierService
        fields = '__all__'
