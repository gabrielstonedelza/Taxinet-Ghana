from rest_framework import serializers

from .models import Wallets, UpdatedWallets


class WalletsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallets
        fields = ['id','user','amount','date_loaded','get_username','get_full_name','get_user_phone']


class UpdatedWalletsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpdatedWallets
        fields = ['id','user','wallet','amount','date_updated','get_username','get_full_name']
        read_only_fields = ['wallet']