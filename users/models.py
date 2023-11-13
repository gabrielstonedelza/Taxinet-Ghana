from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

DeUser = settings.AUTH_USER_MODEL


class User(AbstractUser):
    email = models.EmailField(max_length=255)
    full_name = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=16, unique=True)
    user_tracker_sim = models.CharField(max_length=100, blank=True, default="")
    user_blocked = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['email', 'full_name', 'phone_number', 'user_tracker_sim']
    USERNAME_FIELD = 'username'

    def get_username(self):
        return self.username