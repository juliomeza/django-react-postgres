# server/config/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from enterprise.views import EnterpriseViewSet, ClientViewSet, ProjectViewSet
from materials.views import UOMViewSet, MaterialTypeViewSet, MaterialViewSet, MaterialPriceHistoryViewSet
from inventory.views import InventoryViewSet, InventorySerialNumberViewSet
from logistics.views import AddressViewSet, ContactViewSet, WarehouseViewSet, CarrierViewSet, CarrierServiceViewSet
from orders.views import OrderClassViewSet, OrderTypeViewSet, OrderViewSet, OrderLineViewSet

router = routers.DefaultRouter()
router.register(r'enterprises', EnterpriseViewSet)
router.register(r'owners', ClientViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'uoms', UOMViewSet)
router.register(r'material-types', MaterialTypeViewSet)
router.register(r'materials', MaterialViewSet)
router.register(r'price-history', MaterialPriceHistoryViewSet)
router.register(r'inventories', InventoryViewSet)
router.register(r'serial-numbers', InventorySerialNumberViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'warehouses', WarehouseViewSet)
router.register(r'carriers', CarrierViewSet)
router.register(r'carrier-services', CarrierServiceViewSet)
router.register(r'order-classes', OrderClassViewSet)
router.register(r'order-types', OrderTypeViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-lines', OrderLineViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls')),
    path('api/', include(router.urls)),
]