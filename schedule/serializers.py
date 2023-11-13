from rest_framework import serializers
from .models import ScheduleRide


class ScheduleRideSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')
    admins_username = serializers.SerializerMethodField('get_admins_username')

    class Meta:
        model = ScheduleRide
        fields = ['id','user',
                  'schedule_type', 'schedule_duration','pickup_location','drop_off_location','pick_up_time','start_date','completed','days','status','price','charge','date_scheduled','time_scheduled','pickup_lng','pickup_lat','drop_off_lat','drop_off_lng','get_user_name','get_user_number']
        read_only_fields = ['user']
