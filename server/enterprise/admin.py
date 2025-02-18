from django.contrib import admin
from .models import Enterprise, Owner, Project

@admin.register(Enterprise)
class EnterpriseAdmin(admin.ModelAdmin):
    list_display = ('name', 'lookup_code', 'status')
    search_fields = ('name', 'lookup_code')

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'enterprise')
    search_fields = ('first_name', 'last_name', 'email')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'lookup_code', 'orders_prefix', 'enterprise', 'status')
    search_fields = ('name', 'lookup_code')
