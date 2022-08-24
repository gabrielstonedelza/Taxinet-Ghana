from django.contrib import admin

from .models import (ScheduleRide, Complains, ConfirmDriverPayment, AcceptedScheduledRides,
                     RejectedScheduledRides, DriverVehicleInventory,
                     CompletedScheduledRidesToday, ScheduledNotifications, AssignScheduleToDriver, AcceptAssignedScheduled,
                     RejectAssignedScheduled, CancelScheduledRide, ContactUs, ContactAdmin, PassengersWallet,AskToLoadWallet,AddToUpdatedWallets)

admin.site.register(DriverVehicleInventory)
admin.site.register(ScheduleRide)
admin.site.register(AssignScheduleToDriver)
admin.site.register(AcceptAssignedScheduled)
admin.site.register(RejectAssignedScheduled)
admin.site.register(CancelScheduledRide)
admin.site.register(AcceptedScheduledRides)
admin.site.register(Complains)
admin.site.register(RejectedScheduledRides)
admin.site.register(CompletedScheduledRidesToday)
admin.site.register(ConfirmDriverPayment)
admin.site.register(ScheduledNotifications)
admin.site.register(ContactUs)
admin.site.register(ContactAdmin)
admin.site.register(PassengersWallet)
admin.site.register(AskToLoadWallet)
admin.site.register(AddToUpdatedWallets)
