from rest_framework import viewsets
from .models import UOM, MaterialType, Material, MaterialPriceHistory
from .serializers import (
    UOMSerializer,
    MaterialTypeSerializer,
    MaterialSerializer,
    MaterialPriceHistorySerializer
)

class UOMViewSet(viewsets.ModelViewSet):
    queryset = UOM.objects.all()
    serializer_class = UOMSerializer

class MaterialTypeViewSet(viewsets.ModelViewSet):
    queryset = MaterialType.objects.all()
    serializer_class = MaterialTypeSerializer

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

class MaterialPriceHistoryViewSet(viewsets.ModelViewSet):
    queryset = MaterialPriceHistory.objects.all()
    serializer_class = MaterialPriceHistorySerializer
