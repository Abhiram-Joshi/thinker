from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from .managers import UserManager


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    photo_url = models.URLField()
    uuid = models.UUIDField(unique=True, primary_key=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "uuid"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.username
