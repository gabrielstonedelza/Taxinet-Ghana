from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

from .models import User, DriverProfile, PassengerProfile


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'password', 'user_type', 'phone_number')


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'phone_number')


class DriverProfileSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = DriverProfile
        fields = ['id', 'username', 'user', 'profile_pic', 'fullname', 'drivers_license', 'name_on_licence',
                  'license_number', 'user_profile_pic', 'license_expiration_date', 'license_plate', 'car_name',
                  'car_model', 'ghana_card', 'name_on_ghana_card', 'ghana_card_number', 'verified',
                  'driver_profile_pic', 'get_drivers_license', 'get_ghana_card']
        read_only_fields = ['user']

    def get_username(self, user):
        username = user.user.username
        return username


class PassengerProfileSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = PassengerProfile
        fields = ['id', 'username', 'user', 'profile_pic', 'fullname', 'passenger_profile_pic', 'ghana_card',
                  'name_on_ghana_card', 'ghana_card_number', 'verified',
                  'get_ghana_card', 'next_of_kin', 'next_of_kin_number']
        read_only_fields = ['user']

    def get_username(self, user):
        username = user.user.username
        return username
