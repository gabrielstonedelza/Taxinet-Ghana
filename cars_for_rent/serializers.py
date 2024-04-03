from rest_framework import serializers
from .models import CarsForRent, AddCarImage

class CarsForRentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarsForRent
        fields = ['id','name','engine_type','seater','daily_payment','above_a_week','picture','date_added','get_car_pic']


class AddCarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddCarImage
        fields = ['id','vehicle','image','date_added','get_car_pic']