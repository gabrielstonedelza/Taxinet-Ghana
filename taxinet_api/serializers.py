from rest_framework import serializers
from .models import (Complains,
                     DriversLocation, ConfirmDriverPayment,
                     AcceptedScheduledRides, RejectedScheduledRides, BidScheduleRide, CompletedBidOnScheduledRide,
                     CompletedScheduledRides, ScheduledNotifications, DriverVehicleInventory, Messages, ScheduleRide,
                     AssignScheduleToDriver, AcceptAssignedScheduled,
                     RejectAssignedScheduled, CancelScheduledRide
                     )


class CancelledScheduledRideSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = CancelScheduledRide
        fields = ['id', 'username', 'ride', 'passenger', 'date_cancelled', 'time_cancelled']
        read_only_fields = ['passenger']

    def get_username(self, user):
        username = user.passenger.username
        return username


class RejectScheduleToDriverSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = RejectAssignedScheduled
        fields = ['id', 'username', 'assigned_to_driver', 'driver', 'date_rejected', 'time_rejected']
        read_only_fields = ['driver']

    def get_username(self, user):
        username = user.driver.username
        return username


class AcceptScheduleToDriverSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = AcceptAssignedScheduled
        fields = ['id', 'username', 'assigned_to_driver', 'driver', 'date_accepted', 'time_accepted']
        read_only_fields = ['driver']

    def get_username(self, user):
        username = user.driver.username
        return username


class AssignScheduleToDriverSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = AssignScheduleToDriver
        fields = ['id', 'username', 'ride', 'ride_accepted', 'date_assigned', 'time_assigned']
        read_only_fields = ['driver']

    def get_username(self, user):
        username = user.driver.username
        return username


class AcceptedScheduledRidesSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = AcceptedScheduledRides
        fields = ['id', 'scheduled_ride', 'username', 'driver', 'date_accepted']
        read_only_fields = ['driver']

    def get_username(self, user):
        username = user.driver.username
        return username


class RejectedScheduledRidesSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = RejectedScheduledRides
        fields = ['id', 'scheduled_ride', 'username', 'driver', 'date_rejected']
        read_only_fields = ['driver']

    def get_username(self, user):
        username = user.driver.username
        return username


class MessagesSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = Messages
        fields = ['id', 'user', 'username', 'ride', 'message', 'date_sent', 'time_sent', 'get_profile_pic']
        read_only_fields = ['user', 'ride']

    def get_username(self, user):
        username = user.user.username
        return username


class CompletedScheduledRidesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompletedScheduledRides
        fields = ['id', 'scheduled_ride', 'date_accepted']


class CompletedBidOnScheduledRideSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = CompletedBidOnScheduledRide
        fields = ['id', 'scheduled_ride', 'username', 'driver', 'date_accepted']
        read_only_fields = ['driver']

    def get_username(self, user):
        username = user.driver.username
        return username


class ScheduleRideSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')
    admins_username = serializers.SerializerMethodField('get_admins_username')

    class Meta:
        model = ScheduleRide
        fields = ['id', 'username', 'passenger', 'admins_username', 'administrator', 'schedule_title',
                  'schedule_priority', 'ride_type',
                  'schedule_type', 'schedule_description', 'pick_up_time', 'start_date', 'completed',
                  'pickup_location', 'drop_off_location', 'active', 'price', 'date_scheduled', 'time_scheduled',
                  'get_administrator_profile_pic', 'slug',
                  'get_passenger_profile_pic']
        read_only_fields = ['passenger']

    def get_username(self, user):
        username = user.passenger.username
        return username

    def get_admins_username(self, user):
        admins_username = user.administrator.username
        return admins_username


class BidScheduleRideSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = BidScheduleRide
        fields = ['id', 'username', 'scheduled_ride', 'user', 'bid', 'date_accepted', 'get_profile_pic']
        read_only_fields = ['user', 'scheduled_ride']

    def get_username(self, user):
        username = user.user.username
        return username


class ScheduledNotificationSerializer(serializers.ModelSerializer):
    passengers_username = serializers.SerializerMethodField('get_username')
    drivers_username = serializers.SerializerMethodField('get_driver_username')

    class Meta:
        model = ScheduledNotifications
        fields = ['id', 'notification_id', 'notification_tag', 'notification_title', 'notification_message',
                  'passengers_username', 'drivers_username',
                  'notification_trigger', 'read', 'notification_from', 'notification_to', 'schedule_ride_id',
                  'schedule_ride_accepted_id',
                  'schedule_ride_rejected_id', 'completed_schedule_ride_id', 'message_id',
                  'complain_id', 'reply_id', 'review_id', 'rating_id', 'payment_confirmed_id',
                  'date_created',
                  'passengers_pickup', 'passengers_dropOff', 'get_passengers_notification_from_pic',
                  'drivers_inventory_id']

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


class DriverVehicleInventorySerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = DriverVehicleInventory
        fields = ['id', 'username', 'driver', 'windscreen', 'side_mirror', 'registration_plate', 'tire_pressure',
                  'driving_mirror', 'tire_thread_depth', 'wheel_nuts', 'engine_oil', 'fuel_level', 'break_fluid',
                  'radiator_engine_coolant', 'power_steering_fluid', 'wiper_washer_fluid', 'seat_belts',
                  'steering_wheel', 'horn', 'electric_windows', 'windscreen_wipers', 'head_lights', 'trafficators',
                  'tail_rear_lights', 'reverse_lights', 'interior_lights', 'engine_noise', 'excessive_smoke',
                  'foot_break', 'hand_break', 'wheel_bearing_noise', 'warning_triangle', 'fire_extinguisher',
                  'first_aid_box', 'checked_today', 'date_checked', 'time_checked']
        read_only_fields = ['driver']

    def get_username(self, user):
        username = user.driver.username
        return username
