from rest_framework import serializers
from .models import (Complains,
                     DriversLocation, ConfirmDriverPayment,
                     AcceptedScheduledRides, RejectedScheduledRides,
                     CompletedScheduledRidesToday, ScheduledNotifications, DriverVehicleInventory, ScheduleRide,
                     AssignScheduleToDriver, AcceptAssignedScheduled,
                     RejectAssignedScheduled, CancelScheduledRide, ContactUs, PassengersWallet, AskToLoadWallet
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
        fields = ['id', 'username', 'administrator', 'ride', 'driver', 'ride_accepted', 'date_assigned',
                  'time_assigned']

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


class CompletedScheduledRidesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompletedScheduledRidesToday
        fields = ['id', 'scheduled_ride', 'amount', 'date_accepted', 'get_passenger_username', 'get_amount',
                  'assigned_driver']


class ScheduleRideSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')
    admins_username = serializers.SerializerMethodField('get_admins_username')

    class Meta:
        model = ScheduleRide
        fields = ['id', 'username', 'assigned_driver', 'passenger', 'admins_username', 'administrator',
                  'schedule_title',
                  'schedule_priority', 'ride_type',
                  'schedule_type', 'schedule_description', 'pick_up_time', 'start_date', 'completed',
                  'pickup_location', 'drop_off_location', 'status', 'price', 'initial_payment', 'date_scheduled',
                  'time_scheduled',
                  'get_administrator_profile_pic', 'slug',
                  'get_passenger_profile_pic', 'get_passenger_name', 'get_assigned_driver_name']
        read_only_fields = ['passenger']

    def get_username(self, user):
        username = user.passenger.username
        return username

    def get_admins_username(self, user):
        admins_username = user.administrator.username
        return admins_username


class AdminScheduleRideSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')
    admins_username = serializers.SerializerMethodField('get_admins_username')

    class Meta:
        model = ScheduleRide
        fields = ['id', 'username', 'assigned_driver', 'passenger', 'admins_username', 'administrator',
                  'schedule_title',
                  'schedule_priority', 'ride_type',
                  'schedule_type', 'schedule_description', 'pick_up_time', 'start_date', 'completed',
                  'pickup_location', 'drop_off_location', 'status', 'price', 'initial_payment', 'date_scheduled',
                  'time_scheduled',
                  'get_administrator_profile_pic', 'slug',
                  'get_passenger_profile_pic']

    def get_username(self, user):
        username = user.passenger.username
        return username

    def get_admins_username(self, user):
        admins_username = user.administrator.username
        return admins_username


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
                  'first_aid_box', 'checked_today', 'date_checked', 'time_checked', 'get_drivers_name',
                  'get_driver_profile_pic']
        read_only_fields = ['driver']

    def get_username(self, user):
        username = user.driver.username
        return username


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ['id', 'name', 'email', 'phone', 'message', 'date_sent']


class PassengerWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassengersWallet
        fields = ['id', 'passenger', 'amount', 'date_loaded', 'get_passengers_name', 'get_amount', 'get_passenger_profile_pic']


class AskToLoadWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = AskToLoadWallet
        fields = ['id', 'passenger', 'amount', 'date_requested', 'get_passengers_name', 'get_amount','time_requested']
        read_only_fields = ['passenger']
