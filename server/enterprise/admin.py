from django.contrib import admin
from .models import Enterprise, Client, Project

# @admin.register(Enterprise)
# class EnterpriseAdmin(admin.ModelAdmin):
#     list_display = ('name', 'lookup_code', 'is_active')
#     search_fields = ('name', 'lookup_code')

@admin.register(Client)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'lookup_code', 'is_active', 'enterprise')
    search_fields = ('name', 'lookup_code')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'lookup_code', 'orders_prefix', 'client', 'is_active', 'export_format')
    search_fields = ('name', 'lookup_code')
