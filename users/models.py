from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    """
    Override del usuario
    """
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'  # Usando el campo email para el login
    REQUIRED_FIELDS = []
