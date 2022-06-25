from django.contrib import admin
from .models import DriverProfile, PassengerProfile, User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'user_type', 'full_name', 'phone_number',)


admin.site.register(User, UserAdmin)
admin.site.register(DriverProfile)
admin.site.register(PassengerProfile)
