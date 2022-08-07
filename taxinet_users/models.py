from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.conf import settings
from django.utils import timezone

DeUser = settings.AUTH_USER_MODEL
APP_TYPE = (
    ("Passenger", "Passenger"),
    ("Driver", "Driver"),
    ("Investor", "Investor"),
    ("Administrator", "Administrator"),
)


class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=255)
    user_type = models.CharField(max_length=50, choices=APP_TYPE, default="Passenger")
    full_name = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=16, unique=True)

    REQUIRED_FIELDS = ['user_type', 'email', 'full_name', 'phone_number', ]
    USERNAME_FIELD = 'username'

    def get_username(self):
        return self.username


class AdministratorsProfile(models.Model):
    user = models.OneToOneField(DeUser, on_delete=models.CASCADE, related_name="a_profile")
    profile_pic = models.ImageField(upload_to="profile_pics", default="default_user.png")

    def __str__(self):
        return self.user.username


class DriverProfile(models.Model):
    user = models.OneToOneField(DeUser, on_delete=models.CASCADE, related_name="d_profile")
    profile_pic = models.ImageField(upload_to="profile_pics", default="default_user.png")
    drivers_license = models.ImageField(upload_to="drivers_licenses", blank=True)
    name_on_licence = models.CharField(max_length=100, blank=True)
    license_number = models.CharField(max_length=100, blank=True)
    license_expiration_date = models.CharField(max_length=12, blank=True)
    license_plate = models.CharField(max_length=100, blank=True)
    car_name = models.CharField(max_length=100, blank=True)
    car_model = models.CharField(max_length=100, blank=True)
    front_side_ghana_card = models.ImageField(upload_to="ghana_cards", blank=True)
    back_side_ghana_card = models.ImageField(upload_to="ghana_cards", blank=True)
    name_on_ghana_card = models.CharField(max_length=100, blank=True)
    ghana_card_number = models.CharField(max_length=100, blank=True)
    digital_address = models.CharField(max_length=100, blank=True)
    next_of_kin = models.CharField(max_length=100, blank=True)
    next_of_kin_number = models.CharField(max_length=100, blank=True)
    taxinet_number = models.CharField(max_length=100, default=0)
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username

    def get_user_type(self):
        return self.user.user_type

    def get_front_side_ghana_card(self):
        if self.front_side_ghana_card:
            return "https://taxinetghana.xyz" + self.front_side_ghana_card.url
        return ''

    def get_back_side_ghana_card(self):
        if self.back_side_ghana_card:
            return "https://taxinetghana.xyz" + self.back_side_ghana_card.url
        return ''

    def driver_profile_pic(self):
        if self.profile_pic:
            return "https://taxinetghana.xyz" + self.profile_pic.url
        return ''

    def get_drivers_license(self):
        if self.drivers_license:
            return "https://taxinetghana.xyz" + self.drivers_license.url
        return ''

    def get_drivers_email(self):
        return self.user.email

    def get_drivers_phone_number(self):
        return self.user.phone_number

    def get_drivers_full_name(self):
        return self.user.full_name


class PassengerProfile(models.Model):
    user = models.OneToOneField(DeUser, on_delete=models.CASCADE, related_name="p_profile")
    profile_pic = models.ImageField(upload_to="passenger_profile_pics", default="default_user.png")
    front_side_ghana_card = models.ImageField(upload_to="ghana_cards", blank=True)
    back_side_ghana_card = models.ImageField(upload_to="ghana_cards", blank=True)
    name_on_ghana_card = models.CharField(max_length=100, blank=True)
    next_of_kin = models.CharField(max_length=100, blank=True)
    next_of_kin_number = models.CharField(max_length=100, blank=True)
    referral = models.CharField(max_length=100, blank=True)
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username

    def get_user_type(self):
        return self.user.user_type

    def get_front_side_ghana_card(self):
        if self.front_side_ghana_card:
            return "https://taxinetghana.xyz" + self.front_side_ghana_card.url
        return ''

    def get_back_side_ghana_card(self):
        if self.back_side_ghana_card:
            return "https://taxinetghana.xyz" + self.back_side_ghana_card.url
        return ''

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


class InvestorsProfile(models.Model):
    user = models.OneToOneField(DeUser, on_delete=models.CASCADE, related_name="i_profile")
    profile_pic = models.ImageField(upload_to="investors_profile_pics", default="default_user.png")
    front_side_ghana_card = models.ImageField(upload_to="ghana_cards", blank=True)
    back_side_ghana_card = models.ImageField(upload_to="ghana_cards", blank=True)
    name_on_ghana_card = models.CharField(max_length=100, blank=True)
    next_of_kin = models.CharField(max_length=100, blank=True)
    next_of_kin_number = models.CharField(max_length=100, blank=True)
    referral = models.CharField(max_length=100, blank=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def get_front_side_ghana_card(self):
        if self.front_side_ghana_card:
            return "https://taxinetghana.xyz" + self.front_side_ghana_card.url
        return ''

    def get_back_side_ghana_card(self):
        if self.back_side_ghana_card:
            return "https://taxinetghana.xyz" + self.back_side_ghana_card.url
        return ''

    def investors_profile_pic(self):
        if self.profile_pic:
            return "https://taxinetghana.xyz" + self.profile_pic.url
        return ''

    def get_investors_email(self):
        return self.user.email

    def get_investors_phone_number(self):
        return self.user.phone_number

    def get_investors_full_name(self):
        return self.user.full_name
