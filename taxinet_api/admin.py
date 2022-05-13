from django.contrib import admin

from .models import (RequestRide, BidRide, ScheduleRide, BidScheduleRide, Notifications, Complains, DriverReviews,
                     DriversLocation, DriversPoints, ConfirmDriverPayment,SearchedDestinations)


class RideRequestAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'driver', 'passenger', 'pick_up', 'drop_off', 'ride_accepted', 'ride_rejected', 'price', 'completed',
        'driver_booked', 'date_requested', 'passengers_pick_up_place_id','passengers_drop_off_place_id')


class BidRideAdmin(admin.ModelAdmin):
    list_display = ('id', 'ride', 'user', 'bid', 'date_accepted')


class BidScheduleRideAdmin(admin.ModelAdmin):
    list_display = ('id', 'scheduled_ride', 'user', 'bid', 'date_accepted')


class ScheduleRideAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'passenger', 'driver', 'date_of_pickup', 'time_of_pickup', 'schedule_option', 'pickup_location',
        'drop_off_location',  'scheduled', 'price', 'initial_payment', 'date_scheduled')


admin.site.register(RequestRide, RideRequestAdmin)
admin.site.register(BidRide, BidRideAdmin)
admin.site.register(ScheduleRide, ScheduleRideAdmin)
admin.site.register(BidScheduleRide, BidScheduleRideAdmin)
admin.site.register(Notifications)
admin.site.register(Complains)
admin.site.register(DriverReviews)
admin.site.register(DriversLocation)
admin.site.register(DriversPoints)
admin.site.register(ConfirmDriverPayment)
admin.site.register(SearchedDestinations)
