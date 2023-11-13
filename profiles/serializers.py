from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['id', 'user', 'profile_pic', 'user_profile_pic',  'get_users_email',
                  'get_users_phone_number',
                  'get_users_full_name']
        read_only_fields = ['user']
