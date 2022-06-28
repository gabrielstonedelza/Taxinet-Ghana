from django.contrib import admin

from .models import (RequestRide, BidRide, ScheduleRide, BidScheduleRide, Notifications, Complains, DriverReviews,
                     DriversLocation, DriversPoints, ConfirmDriverPayment, SearchedDestinations, RejectedRides,
                     AcceptedRides, CompletedRides, CompletedBidOnRide, Messages, DriverAnnounceArrival)

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
admin.site.register(RejectedRides)
admin.site.register(AcceptedRides)
admin.site.register(CompletedRides)
admin.site.register(CompletedBidOnRide)
admin.site.register(Messages)
admin.site.register(DriverAnnounceArrival)
