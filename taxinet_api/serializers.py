from rest_framework import serializers
from .models import (RequestRide, BidRide, ScheduleRide, BidScheduleRide, Notifications, Complains, DriverReviews,
                     DriversLocation, DriversPoints, ConfirmDriverPayment, SearchedDestinations, RejectedRides,
                     AcceptedRides, CompletedRides, CompletedBidOnRide, Messages)


class RequestRideSerializer(serializers.ModelSerializer):
    passengers_username = serializers.SerializerMethodField('get_username')
    drivers_username = serializers.SerializerMethodField('get_driver_username')

    class Meta:
        model = RequestRide
        fields = ['id', 'passengers_username', 'drivers_username', 'driver', 'passenger', 'pick_up', 'drop_off',
                  'ride_accepted', 'ride_rejected',
                  'price', 'completed', 'driver_booked', 'date_requested', 'time_requested',
                  'get_driver_profile_pic',
                  'get_passenger_profile_pic', 'passengers_pick_up_place_id', 'passengers_drop_off_place_id',
                  'passengers_lat', 'passengers_lng', 'drop_off_lat', 'drop_off_lng',
                  'driver_on_route', 'passenger_boarded'
                  ]
        read_only_fields = ['passenger']

    def get_username(self, ride):
        passengers_username = ride.passenger.username
        return passengers_username

    def get_driver_username(self, ride):
        drivers_username = ride.driver.username
        return drivers_username


class AcceptedRidesSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = AcceptedRides
        fields = ['id', 'ride', 'username', 'driver', 'passengers_lat', 'passengers_lng', 'date_accepted']
        read_only_fields = ['driver']

    def get_username(self, user):
        username = user.driver.username
        return username


class RejectedRidesSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = RejectedRides
        fields = ['id', 'ride', 'username', 'driver', 'date_rejected']
        read_only_fields = ['driver']

    def get_username(self, user):
        username = user.driver.username
        return username


class BidRideSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = BidRide
        fields = ['id', 'username', 'ride', 'user', 'bid', 'date_accepted', 'get_profile_pic']
        read_only_fields = ['user', 'ride']

    def get_username(self, user):
        username = user.user.username
        return username


class MessagesSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = Messages
        fields = ['id', 'user', 'username', 'ride', 'message', 'date_sent']
        read_only_fields = ['user', 'ride']

    def get_username(self, user):
        username = user.user.username
        return username


class CompletedRidesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompletedRides
        fields = ['id', 'ride', 'date_accepted']


class CompletedBidOnRideSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = CompletedBidOnRide
        fields = ['id', 'ride', 'username', 'driver', 'drivers_lat', 'drivers_lng', 'passengers_pickup',
                  'pick_up_place_id', 'date_accepted']
        read_only_fields = ['driver']

    def get_username(self, user):
        username = user.driver.username
        return username


class ScheduleRideSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')
    drivers_username = serializers.SerializerMethodField('get_drivers_username')

    class Meta:
        model = ScheduleRide
        fields = ['id', 'username', 'passenger', 'drivers_username', 'driver', 'date_of_pickup', 'time_of_pickup',
                  'schedule_option',
                  'pickup_location', 'drop_off_location', 'scheduled', 'price', 'date_scheduled',
                  'get_driver_profile_pic',
                  'get_passenger_profile_pic']
        read_only_fields = ['passenger']

    def get_username(self, user):
        username = user.passenger.username
        return username

    def get_drivers_username(self, user):
        drivers_username = user.driver.username
        return drivers_username


class BidScheduleRideSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = BidScheduleRide
        fields = ['id', 'username', 'scheduled_ride', 'user', 'bid', 'date_accepted', 'get_driver_profile_pic',
                  'get_passenger_profile_pic']
        read_only_fields = ['user', 'scheduled_ride']

    def get_username(self, user):
        username = user.user.username
        return username


class NotificationSerializer(serializers.ModelSerializer):
    passengers_username = serializers.SerializerMethodField('get_username')
    drivers_username = serializers.SerializerMethodField('get_driver_username')

    class Meta:
        model = Notifications
        fields = ['id', 'notification_id', 'notification_tag', 'notification_title', 'notification_message',
                  'passengers_username', 'drivers_username',
                  'notification_trigger', 'read', 'notification_from', 'notification_to', 'ride_id', 'ride_accepted_id',
                  'ride_rejected_id', 'completed_ride_id', 'schedule_ride_id', 'schedule_accepted_id',
                  'schedule_rejected_id', 'complain_id', 'reply_id', 'review_id', 'rating_id', 'payment_confirmed_id',
                  'date_created', 'pick_up_place_id', 'drop_off_place_id', 'passengers_lat', 'passengers_lng',
                  'passengers_pickup', 'passengers_dropOff', 'get_notification_from_profile_pic',
                  'drivers_lat', 'drivers_lng', 'drop_off_lat', 'drop_off_lng',
                  'get_notification_to_profile_pic']

    def get_username(self, notification):
        passengers_username = notification.notification_from.username
        return passengers_username

    def get_driver_username(self, notification):
        drivers_username = notification.notification_to.username
        return drivers_username


class ComplainsSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = Complains
        fields = ['id', 'username', 'complainant', 'offender', 'complain', 'read', 'date_posted']
        read_only_fields = ['complainant']

    def get_username(self, user):
        username = user.complainant.username
        return username


class DriverReviewSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = DriverReviews
        fields = ['id', 'username', 'passenger', 'driver', 'reviews', 'date_posted']
        read_only_fields = ['passenger']

    def get_username(self, user):
        username = user.passenger.username
        return username


class RateDriverSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = DriversPoints
        fields = ['id', 'username', 'passenger', 'driver', 'rating', 'date_rated']
        read_only_fields = ['passenger']

    def get_username(self, user):
        username = user.passenger.username
        return username


class ConfirmDriverPaymentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = ConfirmDriverPayment
        fields = ['id', 'username', 'driver', 'payment_confirmed', 'bank_payment_reference', 'amount', 'date_confirmed',
                  'date_posted']

        read_only_fields = ['driver']

    def get_username(self, user):
        username = user.driver.username
        return username


class DriversLocationSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = DriversLocation
        fields = ['id', 'username', 'driver', 'place_id', 'date_updated', 'get_drivers_pic', 'get_drivers_name',
                  'drivers_plate', 'drivers_car_model', 'drivers_car_name', 'drivers_taxinet_number', 'drivers_lat',
                  'drivers_lng', 'location_name']
        read_only_fields = ['driver']

    def get_username(self, user):
        username = user.driver.username
        return username


class SearchDestinationsSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = SearchedDestinations
        fields = ['id', 'username', 'passenger', 'searched_destination', 'place_id', 'date_searched']
        read_only_fields = ['passenger']

    def get_username(self, user):
        username = user.passenger.username
        return username
