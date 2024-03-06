
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('admin/', admin.site.urls),
    path('car_sales/', include('car_sales.urls')),
    path('deliveries/', include('deliveries.urls')),
    path('drive_pay/', include('drive_pay.urls')),
    path('notifications/', include('notifications.urls')),
    path('pay_drive/', include('pay_drive.urls')),
    path('profiles/', include('profiles.urls')),
    path('schedule/', include('schedule.urls')),
    path('ticketing/', include('ticketing.urls')),
    path('users/', include('users.urls')),
    path('wallets/', include('wallets.urls')),
    path('referrals/', include('referrals.urls')),
    path('inventory/', include('driver_inventory.urls')),
    path('', include('kitchen.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
