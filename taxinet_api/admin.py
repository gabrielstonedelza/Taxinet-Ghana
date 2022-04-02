from django.contrib import admin

from .models import (RequestRide, AcceptRide, ScheduleRide, AcceptScheduleRide, Notifications, Complains, DriverReviews,
                     Sos, RateDriver, ConfirmDriverPayment)


class RideRequestAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'driver', 'passenger', 'pick_up', 'drop_off', 'ride_accepted', 'ride_rejected', 'price', 'completed',
        'driver_status', 'date_requested')


admin.site.register(RequestRide, RideRequestAdmin)
admin.site.register(AcceptRide)
admin.site.register(ScheduleRide)
admin.site.register(AcceptScheduleRide)
admin.site.register(Notifications)
admin.site.register(Complains)
admin.site.register(DriverReviews)
admin.site.register(Sos)
admin.site.register(RateDriver)
admin.site.register(ConfirmDriverPayment)
