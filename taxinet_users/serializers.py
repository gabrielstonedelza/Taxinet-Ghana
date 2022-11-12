from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

from .models import User, DriverProfile, PassengerProfile, AddToVerified, AddCardsUploaded, BigTrucksAdminProfile, \
    RideAdminProfile, PromoterProfile, AccountsProfile, InvestorsProfile


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'password', 'user_type', 'phone_number', 'full_name', 'promoter', 'driver_tracker_sim')


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'phone_number', 'full_name', 'user_type', 'promoter', 'driver_tracker_sim')


class DriverProfileSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = DriverProfile
        fields = ['id', 'username', 'user', 'profile_pic', 'drivers_license', 'name_on_licence',
                  'license_number', 'license_expiration_date', 'license_plate', 'car_name',
                  'car_model', 'front_side_ghana_card', 'get_drivers_full_name',
                  'back_side_ghana_card', 'name_on_ghana_card', 'ghana_card_number', 'digital_address',
                  'next_of_kin', 'next_of_kin_number', 'driver_profile_pic', 'get_drivers_license',
                  'taxinet_number', 'unique_code', 'verified', 'get_front_side_ghana_card', 'get_back_side_ghana_card',
                  'get_drivers_email',
                  'get_drivers_phone_number', 'get_user_type', 'username', 'phone', 'get_driver_tracker_sim_number']
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
                  'get_passengers_full_name', 'unique_code', 'get_user_type', 'username', 'phone', 'promoter',
                  'get_promoter_username', ]
        read_only_fields = ['user']

    def get_username(self, user):
        username = user.user.username
        return username


class AddToVerifiedSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddToVerified
        fields = ['id', 'user', 'date_verified', 'get_passenger_pic']


class AddCardsUploadedSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddCardsUploaded
        fields = ['id', 'user', 'date_uploaded', 'get_passenger_pic']


class AdminPassengerProfileSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = PassengerProfile
        fields = ['id', 'username', 'user', 'profile_pic', 'passenger_profile_pic', 'front_side_ghana_card',
                  'back_side_ghana_card',
                  'name_on_ghana_card', 'next_of_kin', 'next_of_kin_number', 'referral',
                  'verified',
                  'next_of_kin', 'next_of_kin_number', 'get_passengers_email',
                  'get_passengers_phone_number', 'get_front_side_ghana_card', 'get_back_side_ghana_card',
                  'get_passengers_full_name', 'get_user_type', 'promoter', 'get_promoter_username',
                  'get_promoter_phone']

    def get_username(self, user):
        username = user.user.username
        return username


# other serializers

class AccountsProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountsProfile
        fields = ['id', 'get_username', 'user', 'profile_pic', 'passenger_profile_pic',
                  'get_user_type']
        read_only_fields = ['user']


class PromoterProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromoterProfile
        fields = ['id', 'get_username', 'user', 'profile_pic', 'promoter_profile_pic',
                  'get_user_type', 'get_email', 'get_phone_number', 'date_created', 'get_full_name']
        read_only_fields = ['user']


class RideAdminProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideAdminProfile
        fields = ['id', 'get_username', 'user', 'profile_pic', 'passenger_profile_pic',
                  'get_user_type']
        read_only_fields = ['user']


class BigTrucksAdminProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BigTrucksAdminProfile
        fields = ['id', 'get_username', 'user', 'profile_pic', 'passenger_profile_pic',
                  'get_user_type']
        read_only_fields = ['user']


class InvestorsProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestorsProfile
        fields = ['id', 'get_investor_username', 'user', 'profile_pic', 'front_side_ghana_card',
                  'back_side_ghana_card',
                  'name_on_ghana_card', 'next_of_kin', 'next_of_kin_number', 'referral',
                  'verified', 'investors_profile_pic', 'get_investors_email', 'get_investors_phone_number',
                  'get_investors_full_name', 'username', 'phone']
        read_only_fields = ['user']
