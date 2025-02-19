from django.db import models
from django.core.validators import EmailValidator
from common.models import TimeStampedModel, Status

class Address(TimeStampedModel):
    ADDRESS_TYPES = [
        ('shipping', 'Shipping'),
        ('billing', 'Billing'),
    ]
    ENTITY_TYPES = [
        ('enterprise', 'Enterprise'),
        ('warehouse', 'Warehouse'),
        ('recipient', 'Recipient'),
    ]
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    entity_type = models.CharField(max_length=20, choices=ENTITY_TYPES)
    address_type = models.CharField(max_length=10, choices=ADDRESS_TYPES, default='shipping')
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.address_line_1}, {self.city}, {self.state} {self.postal_code}"

class Contact(TimeStampedModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(validators=[EmailValidator()], blank=True)
    mobile = models.CharField(max_length=20, blank=True)
    title = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)
    addresses = models.ManyToManyField(Address, related_name='contacts', blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Warehouse(TimeStampedModel):
    name = models.CharField(max_length=100)
    lookup_code = models.CharField(max_length=50, unique=True)
    address = models.ForeignKey(Address, on_delete=models.PROTECT, related_name='warehouses')
    is_active = models.BooleanField(default=True)
    #status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name='warehouses')
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Carrier(TimeStampedModel):
    name = models.CharField(max_length=100)
    lookup_code = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class CarrierService(TimeStampedModel):
    carrier = models.ForeignKey(Carrier, on_delete=models.PROTECT, related_name='services')
    name = models.CharField(max_length=100)
    lookup_code = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.carrier.name} - {self.name}"
