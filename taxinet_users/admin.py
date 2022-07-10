from django.contrib import admin
from .models import DriverProfile, PassengerProfile, User, AdministratorsProfile, InvestorsProfile

admin.site.register(User)
admin.site.register(DriverProfile)
admin.site.register(PassengerProfile)
admin.site.register(AdministratorsProfile)
admin.site.register(InvestorsProfile)
