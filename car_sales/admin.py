from django.contrib import admin

from .models import Vehicle, AddCarImage, BuyVehicle, AddToApprovedVehiclePurchases


admin.site.register(Vehicle)
admin.site.register(AddCarImage)
admin.site.register(BuyVehicle)
admin.site.register(AddToApprovedVehiclePurchases)
