from pyexpat import model

from rest_framework import serializers
from .models import (Complains,
                     DriversLocation, ConfirmDriverPayment,
                     AcceptedScheduledRides, RejectedScheduledRides,
                     CompletedScheduledRides, ScheduledNotifications, DriverVehicleInventory, ScheduleRide,
                     AssignScheduleToDriver, AcceptAssignedScheduled,
                     RejectAssignedScheduled, CancelScheduledRide, ContactUs, PassengersWallet, AskToLoadWallet,
                     AddToUpdatedWallets, DriverStartTrip, DriverEndTrip, DriverAlertArrival, DriversWallet,
                     DriverAddToUpdatedWallets, DriverAskToLoadWallet, RegisterVehicle, AddToPaymentToday, WorkAndPay,
                     OtherWallet, Wallets, LoadWallet, UpdatedWallets, RideMessages, ExpensesRequest, PrivateChatId,
                  PrivateUserMessage, Stocks, MonthlySalary,
                     PayPromoterCommission, PrivateChatId, AddToBlockList
                     )


class AddToUpdatedWalletsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddToUpdatedWallets
        fields = ['id', 'wallet', 'date_updated']


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
        model = CompletedScheduledRides
        fields = ['id', 'scheduled_ride', 'date_accepted', 'get_passenger_username',
                  'assigned_driver']


class ScheduleRideSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')
    admins_username = serializers.SerializerMethodField('get_admins_username')

    class Meta:
        model = ScheduleRide
        fields = ['id', 'username', 'assigned_driver', 'passenger', 'admins_username', 'administrator',
                  'ride_type',
                  'schedule_type', 'pick_up_time', 'start_date', 'completed',
                  'pickup_location', 'drop_off_location', 'status', 'price', 'charge', 'date_scheduled',
                  'time_scheduled', 'get_passenger_number',
                  'get_administrator_profile_pic', 'slug',
                  'get_passenger_profile_pic', 'get_passenger_name', 'get_assigned_driver_name', 'read',
                  'get_assigned_driver_profile_pic', 'passenger_username',
                  'passenger_phone', 'driver_username', 'driver_phone', 'pickup_lng', 'pickup_lat', 'drop_off_lat',
                  'drop_off_lng']
        read_only_fields = ['passenger']

    def get_username(self, user):
        username = user.passenger.username
        return username

    def get_admins_username(self, user):
        admins_username = user.administrator.username
        return admins_username


class AdminScheduleRideSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleRide
        fields = ['id', 'assigned_driver', 'passenger', 'get_assigned_driver_name', 'administrator',
                  'ride_type',
                  'schedule_type', 'pick_up_time', 'start_date', 'completed',
                  'pickup_location', 'drop_off_location', 'status', 'price', 'charge', 'date_scheduled',
                  'time_scheduled', 'get_passenger_number',
                  'get_administrator_profile_pic', 'slug', 'get_passenger_name',
                  'get_passenger_profile_pic', 'get_assigned_driver_profile_pic', 'passenger_username',
                  'passenger_phone', 'driver_username', 'driver_phone', 'pickup_lng', 'pickup_lat', 'drop_off_lat',
                  'drop_off_lng']


class ScheduledNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduledNotifications
        fields = ['id', 'notification_id', 'notification_tag', 'notification_title', 'notification_message',
                  'notification_trigger', 'read', 'notification_from', 'notification_to', 'schedule_ride_id',
                  'schedule_ride_accepted_id',
                  'schedule_ride_rejected_id', 'completed_schedule_ride_id',
                  'complain_id', 'reply_id', 'review_id', 'rating_id', 'payment_confirmed_id',
                  'date_created',
                  'passengers_pickup', 'passengers_dropOff',
                  'drivers_inventory_id', 'notification_to_passenger']


class ComplainsSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = Complains
        fields = ['id', 'username', 'administrator', 'complainant', 'offender', 'complain', 'read', 'date_posted',
                  'read']
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
        fields = ['id', 'username', 'administrator', 'driver', 'windscreen', 'side_mirror', 'registration_plate',
                  'tire_pressure',
                  'driving_mirror', 'tire_thread_depth', 'wheel_nuts', 'engine_oil', 'fuel_level', 'break_fluid',
                  'radiator_engine_coolant', 'power_steering_fluid', 'wiper_washer_fluid', 'seat_belts',
                  'steering_wheel', 'horn', 'electric_windows', 'windscreen_wipers', 'head_lights', 'trafficators',
                  'tail_rear_lights', 'reverse_lights', 'interior_lights', 'engine_noise', 'excessive_smoke',
                  'foot_break', 'hand_break', 'wheel_bearing_noise', 'warning_triangle', 'fire_extinguisher',
                  'first_aid_box', 'checked_today', 'date_checked', 'time_checked', 'get_drivers_name',
                  'get_driver_profile_pic', 'read', 'registration_number', 'unique_number', 'vehicle_brand', 'millage']
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
        fields = ['id', 'passenger', 'amount', 'date_loaded', 'get_passengers_name', 'get_amount',
                  'get_passenger_profile_pic']


class AskToLoadWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = AskToLoadWallet
        fields = ['id', 'passenger', 'administrator', 'amount', 'date_requested', 'get_passengers_name', 'get_amount',
                  'time_requested',
                  'title', 'read', 'get_passenger_profile_pic']
        read_only_fields = ['passenger']


class DriverStartTripSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverStartTrip
        fields = ['id', 'driver', 'administrator', 'passenger', 'ride', 'date_started', 'time_started']
        read_only_fields = ['driver']


class DriverEndTripSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverEndTrip
        fields = ['id', 'driver', 'administrator', 'passenger', 'ride', 'time_elapsed', 'date_stopped', 'time_stopped',
                  'price',
                  'payment_method']
        read_only_fields = ['driver']


class DriverAlertArrivalSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverAlertArrival
        fields = ['id', 'driver', 'passenger', 'date_alerted', 'time_alerted']
        read_only_fields = ['driver']


# drivers
class DriverAddToUpdatedWalletsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverAddToUpdatedWallets
        fields = ['id', 'wallet', 'date_updated']


class DriversWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriversWallet
        fields = ['id', 'driver', 'amount', 'date_loaded', 'get_drivers_name', 'get_amount',
                  'get_drivers_profile_pic']


class DriverAskToLoadWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverAskToLoadWallet
        fields = ['id', 'driver', 'amount', 'date_requested', 'get_drivers_name', 'get_amount', 'time_requested',
                  'title', 'read', 'get_drivers_profile_pic']
        read_only_fields = ['driver']


class RegisterVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterVehicle
        fields = ['id', 'status', 'brand', 'model', 'color', 'year', 'license_plate_number', 'vin', 'body_number',
                  'registration_certificate_number', 'taxi_license_number', 'transmission', 'boosters',
                  'child_safety_seats', 'code_name', 'category',
                  'date_registered']


class AddToPaymentTodaySerializer(serializers.ModelSerializer):
    class Meta:
        model = AddToPaymentToday
        fields = ['id', 'driver', 'administrator', 'amount', 'title', 'read', 'date_paid', 'time_paid',
                  'get_driver_profile_pic',
                  'get_drivers_full_name', 'username', 'phone']
        read_only_fields = ['driver']


class WorkAndPaySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkAndPay
        fields = ['id', 'driver', 'amount_to_pay', 'amount_paid', 'start_date', 'end_date', 'years', 'fully_paid',
                  'date_started', 'time_started', 'get_assigned_driver_profile_pic', 'get_driver_username']


class OtherWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherWallet
        fields = ['id', 'sender', 'receiver', 'amount', 'date_transferred', 'time_transferred', 'get_profile_pic']
        read_only_fields = ['sender']


# new wallet system
class WalletsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallets
        fields = ['id', 'user', 'amount', 'date_loaded', 'get_profile_pic', 'get_username', 'get_full_name',
                  'get_user_type', 'username', 'phone']


class LoadWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoadWallet
        fields = ['id', 'user', 'title', 'amount', 'date_requested', 'time_requested', 'read', 'get_profile_pic',
                  'get_username', 'get_full_name']
        read_only_fields = ['user']


class UpdatedWalletsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpdatedWallets
        fields = ['id', 'wallet', 'date_updated']


class RideMessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideMessages
        fields = ['id', 'ride', 'user', 'message', 'read', 'date_sent', 'time_sent', 'get_profile_pic', 'get_username',
                  'get_user_type']
        read_only_fields = ['ride']


class ExpensesRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpensesRequest
        fields = ['id', 'guarantor', 'user', 'get_username', 'amount', 'reason', 'request_status', 'date_requested',
                  'time_requested', 'item_name', 'quantity']


# new updates
class AddToBlockListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddToBlockList
        fields = ['id', 'administrator', 'user', 'date_blocked', 'get_username']


class PrivateUserMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivateUserMessage
        fields = ['id', 'sender', 'receiver', 'private_chat_id', 'message', 'read',
                  'get_senders_username', 'get_receivers_username', 'timestamp', 'isSender', 'isReceiver']
        # read_only_fields = ['sender', 'receiver']


class PrivateChatIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivateChatId
        fields = ['id', 'chat_id', 'date_created']


class PayPromoterCommissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayPromoterCommission
        fields = ['id', 'amount', 'promoter', 'date_paid', 'time_paid']


class MonthlySalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlySalary
        fields = ['id', 'driver', 'amount', 'date_paid', 'time_paid']


class StocksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stocks
        fields = ['id', 'item_name', 'quantity', 'date_added', 'time_added']

