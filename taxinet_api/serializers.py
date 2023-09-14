from pyexpat import model

from rest_framework import serializers
from .models import (Complains,RentACar,RegisterCarForRent,
                      ScheduledNotifications, ScheduleRide,RegisteredCarImages,
                      CancelScheduledRide, ContactUs, RegisterVehicle,  Wallets, LoadWallet, UpdatedWallets
                     )


class RegisteredCarImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisteredCarImages
        fields = ['id','registered_car','image','date_added','get_car_picture']
class RegisterCarForRentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterCarForRent
        fields = ['id','name','car_type','number_of_passengers','transmission','air_condition','car_color','date_added','picture','get_car_picture']
class RentACarSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentACar
        fields = ['id','passenger','number_of_days_renting','pick_up_time','pick_up_date','drop_off_time','drop_off_date','rented_car','driver_type','rent_status','date_booked','get_passenger_name','get_passenger_full_name','get_passenger_phone_number','get_rented_car_name','get_car_type','get_car_num_of_passenger','get_car_transmission','get_car_air_condition','get_car_color','get_rented_car_picture']
        read_only_fields = ['passenger']
class CancelledScheduledRideSerializer(serializers.ModelSerializer):

    class Meta:
        model = CancelScheduledRide
        fields = ['id', 'ride', 'passenger', 'date_cancelled', 'time_cancelled']
        read_only_fields = ['passenger']


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
                  'drop_off_lng', 'days', 'get_driver_phone_number']
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
                  'drop_off_lng', 'days', 'get_driver_phone_number']


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


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ['id', 'name', 'email', 'phone', 'message', 'date_sent']


class RegisterVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterVehicle
        fields = ['id', 'status', 'brand', 'model', 'color', 'year', 'license_plate_number', 'vin', 'body_number',
                  'registration_certificate_number', 'taxi_license_number', 'transmission', 'boosters',
                  'child_safety_seats', 'code_name', 'category',
                  'date_registered']


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

