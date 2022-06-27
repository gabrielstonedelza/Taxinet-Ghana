from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

from .models import User, DriverProfile, PassengerProfile


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'password', 'user_type', 'phone_number', 'full_name')


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'phone_number', 'full_name', 'user_type',)


class DriverProfileSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = DriverProfile
        fields = ['id', 'username', 'user', 'profile_pic', 'drivers_license', 'name_on_licence',
                  'license_number', 'license_expiration_date', 'license_plate', 'car_name',
                  'car_model', 'front_side_ghana_card', 'get_drivers_full_name',
                  'back_side_ghana_card', 'name_on_ghana_card', 'ghana_card_number', 'digital_address',
                  'next_of_kin', 'next_of_kin_number', 'driver_profile_pic', 'get_drivers_license',
                  'taxinet_number', 'verified', 'get_front_side_ghana_card', 'get_back_side_ghana_card',
                  'get_drivers_email',
                  'get_drivers_phone_number', ]
        read_only_fields = ['user']

    def get_username(self, user):
        username = user.user.username
        return username


class PassengerProfileSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = PassengerProfile
        fields = ['id', 'username', 'user', 'profile_pic', 'passenger_profile_pic', 'front_side_ghana_card',
                  'back_side_ghana_card',
                  'name_on_ghana_card', 'next_of_kin', 'next_of_kin_number', 'referral',
                  'verified',
                  'next_of_kin', 'next_of_kin_number', 'get_passengers_email',
                  'get_passengers_phone_number', 'get_front_side_ghana_card', 'get_back_side_ghana_card',
                  'get_passengers_full_name']
        read_only_fields = ['user']

    def get_username(self, user):
        username = user.user.username
        return username
