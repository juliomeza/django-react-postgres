from django.db import models
from common.models import TimeStampedModel, Status
from enterprise.models import Project
from logistics.models import Warehouse, Contact, Address, Carrier, CarrierService
from materials.models import Material
from inventory.models import Inventory, InventorySerialNumber

class OrderClass(TimeStampedModel):
    class_name = models.CharField(max_length=50)
    description = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.class_name

class OrderType(TimeStampedModel):
    type_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.type_name

class Order(TimeStampedModel):
    lookup_code_order = models.CharField(
        max_length=50,
        unique=True,
        help_text="Unique order identifier"
    )
    lookup_code_shipment = models.CharField(
        max_length=50,
        unique=True,
        help_text="Unique shipment identifier"
    )
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name='orders')
    order_type = models.ForeignKey(OrderType, on_delete=models.PROTECT, related_name='orders')
    order_class = models.ForeignKey(OrderClass, on_delete=models.PROTECT, related_name='orders')
    project = models.ForeignKey(Project, on_delete=models.PROTECT, related_name='orders')
    warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT, related_name='orders')
    contact = models.ForeignKey(Contact, on_delete=models.PROTECT, related_name='orders')
    shipping_address = models.ForeignKey(Address, on_delete=models.PROTECT, related_name='shipping_orders')
    billing_address = models.ForeignKey(Address, on_delete=models.PROTECT, related_name='billing_orders')
    carrier = models.ForeignKey(Carrier, on_delete=models.PROTECT, related_name='orders', null=True, blank=True)
    service_type = models.ForeignKey(CarrierService, on_delete=models.PROTECT, related_name='orders', null=True, blank=True)
    expected_delivery_date = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.order_type} - {self.lookup_code_order}"

class OrderLine(TimeStampedModel):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name='lines')
    material = models.ForeignKey(Material, on_delete=models.PROTECT, related_name='order_lines')
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    license_plate = models.ForeignKey(
        Inventory,
        on_delete=models.PROTECT,
        related_name='order_lines',
        null=True, blank=True
    )
    serial_number = models.ForeignKey(
        InventorySerialNumber,
        on_delete=models.PROTECT,
        related_name='order_lines',
        null=True, blank=True
    )
    lot = models.CharField(max_length=50, blank=True)
    vendor_lot = models.CharField(max_length=50, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Order {self.order.lookup_code_order} - {self.material.name} ({self.quantity})"
