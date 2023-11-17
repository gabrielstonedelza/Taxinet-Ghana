from django.contrib import admin

from .models import Vehicle, AddCarImage, BuyVehicle, AddToApprovedVehiclePurchases

class AdminBuyVehicleModel(admin.ModelAdmin):
    list_display = ['id','user','vehicle','request_approved','date_requested']

    class Meta:
        model = BuyVehicle

class AdminAddToApprovedVehiclePurchases(admin.ModelAdmin):
    list_display = ['id','user','vehicle','date_approved']

    class Meta:
        model = AddToApprovedVehiclePurchases


class AdminVehicleModel(admin.ModelAdmin):
    list_display = "__all__"
    class Meta:
        model = Vehicle

admin.site.register(Vehicle)
admin.site.register(AddCarImage)
admin.site.register(BuyVehicle,AdminBuyVehicleModel)
admin.site.register(AddToApprovedVehiclePurchases,AdminAddToApprovedVehiclePurchases)
