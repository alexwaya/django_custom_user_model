# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # add additional fields in here
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    
    leave_days = models.CharField(max_length=50)

    def __str__(self):
        return self.email