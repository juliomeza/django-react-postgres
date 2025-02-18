from django.contrib.auth.models import AbstractUser
from django.db import models
from common.models import TimeStampedModel

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

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
