from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Role

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('role_name', 'created_date', 'modified_date')
    search_fields = ('role_name',)

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):  # Usa UserAdmin en lugar de ModelAdmin
    list_display = ('email', 'first_name', 'last_name', 'role', 'is_staff', 'is_active')
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ()

    # Orden y organización de los campos en el formulario de edición
    fieldsets = (
        ("Personal Information", {'fields': ('first_name', 'last_name', 'email', 'password')}),
        ("User Details", {'fields': ('username', 'role')}),
        ("Permissions", {'fields': ('is_staff', 'is_active', 'is_superuser', 'user_permissions')}),
        ("Fechas Importantes", {'fields': ('last_login', 'date_joined')}),
    )

    # Orden en el formulario de creación de usuario en Django Admin
    add_fieldsets = (
        ("Personal Information", {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'username', 'password1', 'password2', 'role'),
        }),
        ("Permissions", {'fields': ('is_staff', 'is_active')}),
    )

    ordering = ('email',)