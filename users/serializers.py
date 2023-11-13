from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

from .models import User

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'password', 'phone_number', 'full_name', 'user_tracker_sim', 'user_blocked')


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'phone_number', 'full_name','user_tracker_sim', 'user_blocked',)





