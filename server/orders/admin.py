from django.contrib import admin
from .models import OrderClass, OrderType, Order, OrderLine

@admin.register(OrderClass)
class OrderClassAdmin(admin.ModelAdmin):
    list_display = ('class_name', 'is_active', 'created_date')
    search_fields = ('class_name',)

@admin.register(OrderType)
class OrderTypeAdmin(admin.ModelAdmin):
    list_display = ('type_name', 'created_date')
    search_fields = ('type_name',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('lookup_code_order', 'order_type', 'project', 'status', 'expected_delivery_date')
    search_fields = ('lookup_code_order', 'lookup_code_shipment')

@admin.register(OrderLine)
class OrderLineAdmin(admin.ModelAdmin):
    list_display = ('order', 'material', 'quantity')
    search_fields = ('order__lookup_code_order', 'material__name')
