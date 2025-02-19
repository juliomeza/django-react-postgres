# server/config/urls.py
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from enterprise.views import EnterpriseViewSet, ClientViewSet, ProjectViewSet
from materials.views import UOMViewSet, MaterialTypeViewSet, MaterialViewSet, MaterialPriceHistoryViewSet
from inventory.views import InventoryViewSet, InventorySerialNumberViewSet
from logistics.views import AddressViewSet, ContactViewSet, WarehouseViewSet, CarrierViewSet, CarrierServiceViewSet
from orders.views import OrderClassViewSet, OrderTypeViewSet, OrderViewSet, OrderLineViewSet

# Swagger Configuration
schema_view = get_schema_view(
    openapi.Info(
        title="SupplyGrid API",
        default_version="v1",
        description="Documentación de la API de órdenes y logística",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contacto@example.com"),
        license=openapi.License(name="Licencia MIT"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Configure routers with ViewSets
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

    # Rutas para Swagger y Redoc
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^swagger\.json$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]