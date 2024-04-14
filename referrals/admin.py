from django.contrib import admin

from .models import Referrals, ReferralWallets, UpdatedReferralWallets

admin.site.register(Referrals)
admin.site.register(ReferralWallets)
admin.site.register(UpdatedReferralWallets)
