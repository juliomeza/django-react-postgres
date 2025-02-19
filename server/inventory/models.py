from django.db import models
from django.core.validators import MinLengthValidator
from common.models import TimeStampedModel, Status
from enterprise.models import Project
from logistics.models import Warehouse
from materials.models import Material

class Inventory(TimeStampedModel):
    project = models.ForeignKey(Project, on_delete=models.PROTECT, related_name='inventories')
    warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT, related_name='inventories')
    material = models.ForeignKey(Material, on_delete=models.PROTECT, related_name='inventories')
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=50, blank=True)
    license_plate_id = models.CharField(
        max_length=50,
        unique=True,
        blank=True,
        validators=[MinLengthValidator(2)]
    )
    license_plate = models.CharField(max_length=50, blank=True)
    lot = models.CharField(max_length=50, blank=True)
    vendor_lot = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.license_plate}"

class InventorySerialNumber(TimeStampedModel):
    lookup_code = models.CharField(max_length=50, unique=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name='serial_numbers')
    license_plate = models.ForeignKey(Inventory, on_delete=models.PROTECT, related_name='serial_numbers')
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"SN: {self.lookup_code}"
