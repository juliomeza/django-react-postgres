from django.contrib import admin
from .models import Inventory, InventorySerialNumber

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('project', 'warehouse', 'material', 'license_plate_id', 'quantity')
    search_fields = ('license_plate_id',)

@admin.register(InventorySerialNumber)
class InventorySerialNumberAdmin(admin.ModelAdmin):
    list_display = ('lookup_code', 'license_plate', 'status')
    search_fields = ('lookup_code',)
