from django.db import models
from users.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="p_profile")
    profile_pic = models.ImageField(upload_to="profile_pics", default="default_user.png")
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def user_profile_pic(self):
        if self.profile_pic:
            return "https://taxinetghana.xyz" + self.profile_pic.url
        return ''

    def get_users_email(self):
        return self.user.email

    def get_users_phone_number(self):
        return self.user.phone_number

    def get_users_full_name(self):
        return self.user.full_name

    def get_username(self):
        return self.user.username

