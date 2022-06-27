from django.contrib import admin
from .models import DriverProfile, PassengerProfile, User

admin.site.register(User)
admin.site.register(DriverProfile)
admin.site.register(PassengerProfile)
