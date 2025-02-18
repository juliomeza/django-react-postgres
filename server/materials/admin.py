from django.contrib import admin
from .models import UOM, MaterialType, Material, MaterialPriceHistory

@admin.register(UOM)
class UOMAdmin(admin.ModelAdmin):
    list_display = ('name', 'lookup_code')
    search_fields = ('name', 'lookup_code')

@admin.register(MaterialType)
class MaterialTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'lookup_code')
    search_fields = ('name', 'lookup_code')

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'lookup_code', 'project', 'status', 'type', 'uom')
    search_fields = ('name', 'lookup_code')

@admin.register(MaterialPriceHistory)
class MaterialPriceHistoryAdmin(admin.ModelAdmin):
    list_display = ('material', 'price', 'effective_date', 'end_date')
    search_fields = ('material__name',)
