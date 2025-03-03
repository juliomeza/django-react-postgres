from django.contrib import admin
from .models import Address, Contact, Warehouse, Carrier, CarrierService

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('address_line_1', 'city', 'state', 'postal_code', 'country', 'entity_type', 'address_type')
    search_fields = ('address_line_1', 'city', 'state', 'postal_code', 'country')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'contact_name', 'phone', 'email')
    search_fields = ('company_name', 'contact_name', 'email', 'phone')

@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'lookup_code', 'address', 'is_active')
    search_fields = ('name', 'lookup_code')

@admin.register(Carrier)
class CarrierAdmin(admin.ModelAdmin):
    list_display = ('name', 'lookup_code')
    search_fields = ('name', 'lookup_code')

@admin.register(CarrierService)
class CarrierServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'lookup_code', 'carrier')
    search_fields = ('name', 'lookup_code', 'carrier__name')
