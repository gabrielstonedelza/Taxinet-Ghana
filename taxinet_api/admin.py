from django.contrib import admin

from .models import (ScheduleRide, Complains, ConfirmDriverPayment, Messages, AcceptedScheduledRides,
                     RejectedScheduledRides, BidScheduleRide, CompletedBidOnScheduledRide, DriverVehicleInventory,
                     CompletedScheduledRides, ScheduledNotifications)

admin.site.register(DriverVehicleInventory)
admin.site.register(BidScheduleRide)
admin.site.register(ScheduleRide)

admin.site.register(AcceptedScheduledRides)
admin.site.register(Complains)
admin.site.register(RejectedScheduledRides)
admin.site.register(CompletedBidOnScheduledRide)
admin.site.register(CompletedScheduledRides)
admin.site.register(ConfirmDriverPayment)
admin.site.register(ScheduledNotifications)

