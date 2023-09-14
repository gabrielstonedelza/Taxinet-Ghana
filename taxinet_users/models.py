from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

DeUser = settings.AUTH_USER_MODEL
APP_TYPE = (
    ("Passenger", "Passenger"),
    ("Administrator", "Administrator"),
)


class User(AbstractUser):
    email = models.EmailField(max_length=255)
    user_type = models.CharField(max_length=50, choices=APP_TYPE, default="Passenger")
    full_name = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=16, unique=True)
    driver_tracker_sim = models.CharField(max_length=100, blank=True, default="")
    user_blocked = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['user_type', 'email', 'full_name', 'phone_number', 'driver_tracker_sim']
    USERNAME_FIELD = 'username'

    def get_username(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(DeUser, on_delete=models.CASCADE, related_name="p_profile")
    profile_pic = models.ImageField(upload_to="profile_pics", default="default_user.png")
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username

    def get_user_type(self):
        return self.user.user_type

    def passenger_profile_pic(self):
        if self.profile_pic:
            return "https://taxinetghana.xyz" + self.profile_pic.url
        return ''

    def get_passengers_email(self):
        return self.user.email

    def get_passengers_phone_number(self):
        return self.user.phone_number

    def get_passengers_full_name(self):
        return self.user.full_name

