from rest_framework import serializers
from .models import UOM, MaterialType, Material, MaterialPriceHistory

class UOMSerializer(serializers.ModelSerializer):
    class Meta:
        model = UOM
        fields = '__all__'

class MaterialTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialType
        fields = '__all__'

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'

class MaterialPriceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialPriceHistory
        fields = '__all__'
