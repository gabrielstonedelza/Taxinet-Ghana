from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from PIL import Image

DeUser = settings.AUTH_USER_MODEL
APP_TYPE = (
    ("Driver", "Driver"),
    ("Passenger", "Passenger"),
)


class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=255)
    user_type = models.CharField(max_length=50, choices=APP_TYPE, default="Passenger")
    phone_number = models.CharField(max_length=16, unique=True)
    unique_code = models.CharField(max_length=100)

    REQUIRED_FIELDS = ['email', 'user_type', 'phone_number']
    USERNAME_FIELD = 'username'

    def get_username(self):
        return self.username


class DriverProfile(models.Model):
    user = models.OneToOneField(DeUser, on_delete=models.CASCADE, related_name="d_profile")
    profile_pic = models.ImageField(upload_to="profile_pics", default="default_user.png")
    fullname = models.CharField(max_length=150, blank=True)
    drivers_license = models.ImageField(upload_to="drivers_licenses", blank=True)
    name_on_licence = models.CharField(max_length=100, blank=True)
    license_number = models.CharField(max_length=100, blank=True)
    license_expiration_date = models.DateField(blank=True)
    license_plate = models.CharField(max_length=100, blank=True)
    car_name = models.CharField(max_length=100, blank=True)
    car_model = models.CharField(max_length=100, blank=True)
    ghana_card = models.ImageField(upload_to="ghana_cards", blank=True)
    name_on_ghana_card = models.CharField(max_length=100, blank=True)
    ghana_card_number = models.CharField(max_length=100, blank=True)
    digital_address = models.CharField(max_length=100, blank=True)
    next_of_kin = models.CharField(max_length=100, blank=True)
    next_of_kin_number = models.CharField(max_length=100)
    verified = models.BooleanField(default=False)
    share_ride = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.profile_pic.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)

    def driver_profile_pic(self):
        if self.profile_pic:
            return "http://127.0.0.1:8000" + self.profile_pic.url
        return ''

    def get_drivers_license(self):
        if self.drivers_license:
            return "http://127.0.0.1:8000" + self.drivers_license.url
        return ''

    def get_ghana_card(self):
        if self.ghana_card:
            return "http://127.0.0.1:8000" + self.ghana_card.url
        return ''


class PassengerProfile(models.Model):
    user = models.OneToOneField(DeUser, on_delete=models.CASCADE, related_name="p_profile")
    profile_pic = models.ImageField(upload_to="passenger_profile_pics", default="default_user.png")
    fullname = models.CharField(max_length=150, blank=True)
    ghana_card = models.ImageField(upload_to="ghana_cards", blank=True)
    name_on_ghana_card = models.CharField(max_length=100, blank=True)
    ghana_card_number = models.CharField(max_length=100, blank=True)
    verified = models.BooleanField(default=False)
    next_of_kin = models.CharField(max_length=100, blank=True)
    next_of_kin_number = models.CharField(max_length=100, blank=True)
    referral = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.profile_pic.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)

    def get_ghana_card(self):
        if self.ghana_card:
            return "http://127.0.0.1:8000" + self.ghana_card.url
        return ''

    def passenger_profile_pic(self):
        if self.profile_pic:
            return "http://127.0.0.1:8000" + self.profile_pic.url
        return ''
