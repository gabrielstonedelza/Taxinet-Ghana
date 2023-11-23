from rest_framework import serializers
from .models import DriverVehicleInventory


class DriverVehicleInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverVehicleInventory
        fields = ['id','user','millage','windscreen','side_mirror','registration_plate','tire_pressure','driving_mirror','tire_thread_depth','wheel_nuts','engine_oil','fuel_level','break_fluid','radiator_engine_coolant','power_steering_fluid','wiper_washer_fluid','seat_belts','steering_wheel','horn','electric_windows','windscreen_wipers','head_lights','trafficators','tail_rear_lights','reverse_lights','interior_lights','engine_noise','excessive_smoke','foot_break','hand_break','wheel_bearing_noise','warning_triangle','fire_extinguisher','first_aid_box','checked_today','date_checked','time_checked','get_user_name']

        read_only_fields = ['user']