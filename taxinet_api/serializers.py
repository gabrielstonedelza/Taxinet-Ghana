from rest_framework import serializers
from .models import (RequestRide, AcceptRide, ScheduleRide, AcceptScheduleRide, Notifications, Complains, DriverReviews, \
                     Sos, RateDriver, ConfirmDriverPayment)


class RequestRideSerializer(serializers.ModelSerializer):
    passengers_username = serializers.SerializerMethodField('get_username')
    drivers_username = serializers.SerializerMethodField('get_driver_username')

    class Meta:
        model = RequestRide
        fields = ['id', 'passengers_username', 'drivers_username', 'driver', 'passenger', 'pick_up', 'drop_off',
                  'ride_accepted', 'ride_rejected',
                  'price', 'completed', 'driver_status', 'date_requested', 'get_driver_profile_pic',
                  'get_passenger_profile_pic']
        read_only_fields = ['passenger']

    def get_username(self, user):
        passengers_username = user.passenger.username
        return passengers_username

    def get_driver_username(self, user):
        drivers_username = user.driver.username
        return drivers_username


class AcceptRideSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = AcceptRide
        fields = ['id', 'username', 'ride', 'user', 'bid', 'price', 'accept', 'reject_ride', 'driver_approved',
                  'passenger_approved', 'date_accepted', 'get_driver_profile_pic',
                  'get_passenger_profile_pic']
        read_only_fields = ['user']

    def get_username(self, user):
        username = user.user.username
        return username


class ScheduleRideSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')
    drivers_username = serializers.SerializerMethodField('get_drivers_username')

    class Meta:
        model = ScheduleRide
        fields = ['id', 'username', 'passenger', 'drivers_username', 'driver', 'date_of_pickup', 'time_of_pickup',
                  'schedule_option',
                  'pickup_location', 'drop_off_location', 'confirmation_status', 'scheduled', 'price', 'date_scheduled',
                  'get_driver_profile_pic',
                  'get_passenger_profile_pic']
        read_only_fields = ['passenger']

    def get_username(self, user):
        username = user.passenger.username
        return username

    def get_drivers_username(self, user):
        drivers_username = user.driver.username
        return drivers_username


class AcceptScheduleRideSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = AcceptScheduleRide
        fields = ['id', 'username', 'scheduled_ride', 'user', 'bid', 'price', 'accept', 'reject_scheduled',
                  'driver_approved', 'passenger_approved', 'date_accepted', 'get_driver_profile_pic',
                  'get_passenger_profile_pic']
        read_only_fields = ['user']

    def get_username(self, user):
        username = user.user.username
        return username


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = ['id', 'notification_id', 'notification_tag', 'notification_title', 'notification_message',
                  'notification_trigger', 'read', 'notification_from', 'notification_to', 'ride_id', 'ride_accepted_id',
                  'ride_rejected_id', 'completed_ride_id', 'schedule_ride_id', 'schedule_accepted_id',
                  'schedule_rejected_id', 'complain_id', 'reply_id', 'review_id', 'rating_id', 'payment_confirmed_id',
                  'date_created', 'get_notification_from_profile_pic', 'get_notification_to_profile_pic']


class ComplainsSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = Complains
        fields = ['id', 'username', 'complainant', 'offender', 'complain', 'reply', 'read', 'date_posted',
                  'get_complainant_profile_pic', 'get_offender_profile_pic']
        read_only_fields = ['complainant']

    def get_username(self, user):
        username = user.complainant.username
        return username


class DriverReviewSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = DriverReviews
        fields = ['id', 'username', 'passenger', 'driver', 'reviews', 'date_posted', 'get_passenger_profile_pic',
                  'get_driver_profile_pic']
        read_only_fields = ['passenger']

    def get_username(self, user):
        username = user.passenger.username
        return username


class RateDriverSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = RateDriver
        fields = ['id', 'username', 'passenger', 'driver', 'rating', 'date_rated']
        read_only_fields = ['passenger']

    def get_username(self, user):
        username = user.passenger.username
        return username


class ConfirmDriverPaymentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = ConfirmDriverPayment
        fields = ['id', 'username', 'driver', 'payment_confirmed', 'bank_payment_reference', 'amount', 'date_confirmed']

        read_only_fields = ['driver']

    def get_username(self, user):
        username = user.driver.username
        return username
