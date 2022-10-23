from django.contrib import admin
from .models import (DriverProfile, PassengerProfile, User, AdministratorsProfile, InvestorsProfile, AddToVerified, AddCardsUploaded, BigTrucksAdminProfile, RideAdminProfile, PromoterProfile, AccountsProfile)

admin.site.register(User)
admin.site.register(BigTrucksAdminProfile)
admin.site.register(RideAdminProfile)
admin.site.register(PromoterProfile)
admin.site.register(AccountsProfile)
admin.site.register(DriverProfile)
admin.site.register(PassengerProfile)
admin.site.register(AdministratorsProfile)
admin.site.register(InvestorsProfile)
admin.site.register(AddToVerified)
admin.site.register(AddCardsUploaded)

