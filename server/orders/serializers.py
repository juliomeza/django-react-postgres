from rest_framework import serializers
from .models import OrderClass, OrderType, Order, OrderLine

class OrderClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderClass
        fields = '__all__'

class OrderTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderType
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderLine
        fields = '__all__'
