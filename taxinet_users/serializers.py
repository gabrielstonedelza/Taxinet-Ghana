from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

from .models import User,  Profile

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'password', 'user_type', 'phone_number', 'full_name', 'driver_tracker_sim', 'user_blocked')


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'phone_number', 'full_name', 'user_type','driver_tracker_sim', 'user_blocked',)


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['id', 'user', 'profile_pic', 'passenger_profile_pic',  'get_passengers_email',
                  'get_passengers_phone_number',
                  'get_passengers_full_name',  'get_user_type', 'phone' ]
        read_only_fields = ['user']




