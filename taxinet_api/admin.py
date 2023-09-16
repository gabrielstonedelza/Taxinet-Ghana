from django.contrib import admin

from .models import (ScheduleRide, Complains,  ScheduledNotifications,  CancelScheduledRide, ContactUs, ContactAdmin, RegisterVehicle,RentACar,RegisteredCarImages,RegisterCarForRent,
                     Wallets, UpdatedWallets)


class AdminScheduleRide(admin.ModelAdmin):
    list_display = ['id', 'administrator', 'passenger', 'schedule_type','schedule_duration',
                 'pickup_location', 'drop_off_location', 'pick_up_time',
                    'start_date', 'status', 'price', 'charge', 'date_scheduled']
    search_fields = ['id', 'passenger', 'assigned_driver']

    class Meta:
        model = ScheduleRide

admin.site.register(RentACar)
admin.site.register(RegisteredCarImages)
admin.site.register(RegisterCarForRent)

admin.site.register(UpdatedWallets)

admin.site.register(ScheduleRide, AdminScheduleRide)

admin.site.register(CancelScheduledRide)

admin.site.register(Complains)

admin.site.register(ScheduledNotifications)
admin.site.register(ContactUs)
admin.site.register(ContactAdmin)

admin.site.register(RegisterVehicle)
admin.site.register(Wallets)
