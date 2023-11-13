
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
