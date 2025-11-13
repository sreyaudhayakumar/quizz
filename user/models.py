from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom user model extending Django default user.
    """
    class UserRoles(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        USER = "USER", "Normal User"

    role = models.CharField(
        max_length=10,
        choices=UserRoles.choices,
        default=UserRoles.USER
    )

    def __str__(self):
        return f"{self.username} ({self.role})"
