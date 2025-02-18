from django.db import models
from django.core.validators import MinLengthValidator
from common.models import TimeStampedModel, Status
from enterprise.models import Project

class UOM(TimeStampedModel):
    name = models.CharField(max_length=50)
    lookup_code = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.name} ({self.lookup_code})"

class MaterialType(TimeStampedModel):
    name = models.CharField(max_length=50)
    lookup_code = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Material(TimeStampedModel):
    name = models.CharField(max_length=100)
    lookup_code = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=100, blank=True)
    project = models.ForeignKey(Project, on_delete=models.PROTECT, related_name='materials')
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name='materials')
    type = models.ForeignKey(MaterialType, on_delete=models.PROTECT, related_name='materials')
    uom = models.ForeignKey(UOM, on_delete=models.PROTECT, related_name='materials')
    is_serialized = models.BooleanField(default=False)

    def current_price(self):
        price_history = self.price_history.filter(effective_date__lte=models.functions.Now()).order_by('-effective_date').first()
        return price_history.price if price_history else None

    def __str__(self):
        return self.name

class MaterialPriceHistory(TimeStampedModel):
    material = models.ForeignKey(Material, on_delete=models.PROTECT, related_name='price_history')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    effective_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.material.name} - ${self.price} (from {self.effective_date.date()})"
