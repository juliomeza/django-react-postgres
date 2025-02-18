# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class CustomUser(AbstractUser):
#     """
#     Custom user model extending Django's AbstractUser
#     """
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.EmailField(unique=True)

#     # Definir USERNAME_FIELD para que los usuarios inicien sesión con email en lugar de username
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

#     class Meta:
#         indexes = [
#             models.Index(fields=['email', 'username']),
#         ]

#     def __str__(self):
#         return f"{self.first_name} {self.last_name} ({self.email})"

#     def get_full_name(self):
#         return f"{self.first_name} {self.last_name}"

#     def get_short_name(self):
#         return self.first_name

from django.contrib.auth.models import AbstractUser
from django.db import models
from common.models import TimeStampedModel
from enterprise.models import Project

class Role(TimeStampedModel):
    role_name = models.CharField(max_length=50, unique=True)
    permissions = models.JSONField(help_text="JSON field storing permitted actions")

    def __str__(self):
        return self.role_name

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    role = models.ForeignKey(
        Role,
        on_delete=models.PROTECT,
        related_name="users",
        null=True, blank=True
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.PROTECT,
        related_name="users",
        null=True, blank=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
