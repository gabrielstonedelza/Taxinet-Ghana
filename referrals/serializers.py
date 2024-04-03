from rest_framework import serializers
from .models import Referrals, ReferralWallets,UpdatedReferralWallets

class ReferralsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referrals
        fields = ['id','name','phone','date_added']

class ReferralWalletsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferralWallets
        fields = ['referral','amount','date_loaded','get_referral_phone','get_referral_name']

class UpdatedReferralWalletsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpdatedReferralWallets
        fields = ['id','referral','referral_wallet','amount','date_updated','get_name']
        read_only_fields = ['referral_wallet']