from django.db import models
from django.core.validators import MinLengthValidator
from common.models import TimeStampedModel
from logistics.models import Address
from django.contrib.auth import get_user_model

class Enterprise(TimeStampedModel):
    name = models.CharField(max_length=100)
    lookup_code = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    #status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name="enterprises")
    address = models.ForeignKey(
        Address,
        on_delete=models.PROTECT,
        related_name="enterprises",
        null=True, blank=True
    )
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Client(TimeStampedModel):
    name = models.CharField(max_length=100)
    lookup_code = models.CharField(max_length=50, unique=True)
    address = models.ForeignKey(
        Address,
        on_delete=models.PROTECT,
        related_name="clients",
        null=True, blank=True
    )
    enterprise = models.ForeignKey(
        Enterprise,
        on_delete=models.PROTECT,
        related_name="clients"
    )
    is_active = models.BooleanField(default=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Project(TimeStampedModel):
    name = models.CharField(max_length=100)
    lookup_code = models.CharField(max_length=50, unique=True)
    orders_prefix = models.CharField(
        max_length=10,
        unique=True,
        validators=[MinLengthValidator(2)],
        help_text="Unique prefix for order numbers"
    )
    client = models.ForeignKey(
        Client,
        on_delete=models.PROTECT,
        related_name="projects"
    )
    users = models.ManyToManyField(get_user_model(), related_name="projects")
    is_active = models.BooleanField(default=True)
    notes = models.TextField(blank=True)
    # Relaciones opcionales con logística:
    warehouses = models.ManyToManyField('logistics.Warehouse', related_name="projects", blank=True)
    carriers = models.ManyToManyField('logistics.Carrier', related_name="projects", blank=True)
    services = models.ManyToManyField('logistics.CarrierService', related_name="projects", blank=True)
    contacts = models.ManyToManyField('logistics.Contact', related_name="projects", blank=True)

    def __str__(self):
        return self.name
