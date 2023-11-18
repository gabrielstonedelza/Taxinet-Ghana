from django.contrib import admin

from .models import Wallets,UpdatedWallets

class AdminWallet(admin.ModelAdmin):
    list_display = ['id','user','amount','date_loaded']
    class Meta:
        model = Wallets


class AdminUpdatedWallets(admin.ModelAdmin):
    list_display = ['id','user','wallet','amount','date_updated']
    class Meta:
        model = UpdatedWallets

admin.site.register(Wallets,AdminWallet)
admin.site.register(UpdatedWallets,AdminUpdatedWallets)
