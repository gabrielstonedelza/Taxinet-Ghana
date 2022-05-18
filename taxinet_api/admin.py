from django.contrib import admin

from .models import (RequestRide, BidRide, ScheduleRide, BidScheduleRide, Notifications, Complains, DriverReviews,
                     DriversLocation, DriversPoints, ConfirmDriverPayment,SearchedDestinations)


admin.site.register(RequestRide)
admin.site.register(BidRide)
admin.site.register(ScheduleRide)
admin.site.register(BidScheduleRide)
admin.site.register(Notifications)
admin.site.register(Complains)
admin.site.register(DriverReviews)
admin.site.register(DriversLocation)
admin.site.register(DriversPoints)
admin.site.register(ConfirmDriverPayment)
admin.site.register(SearchedDestinations)
