from django.shortcuts import render
from django.http import Http404
from decimal import Decimal
from django.shortcuts import get_object_or_404
from rest_framework import permissions, generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Referrals, ReferralWallets,UpdatedReferralWallets
from .serializers import ReferralsSerializer, ReferralWalletsSerializer, UpdatedReferralWalletsSerializer

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def add_new_referral(request):
    serializer = ReferralsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_referrals(request):
    referrals = Referrals.objects.all().order_by('-date_added')
    serializer = ReferralsSerializer(referrals, many=True)
    return Response(serializer.data)


# referral wallet
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def create_referrals_wallet(request):
    serializer = ReferralWalletsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
@permission_classes([permissions.AllowAny])
def update_referral_wallet(request, id,amount_to_update):
    wallet = get_object_or_404(ReferralWallets, id=id)
    serializer = ReferralWalletsSerializer(wallet, data=request.data)
    if serializer.is_valid():
        if wallet:
            UpdatedReferralWallets.objects.create(referral=wallet.user, referral_wallet=wallet, amount=amount_to_update)
            wallet.amount = wallet.amount + Decimal(amount_to_update)
            wallet.save()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_referrals_wallets(request):
    wallets = ReferralWallets.objects.all().order_by('-date_added')
    serializer = ReferralWalletsSerializer(wallets, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_referrals_updated_wallets(request):
    wallets = UpdatedReferralWallets.objects.all().order_by('-date_added')
    serializer = UpdatedReferralWalletsSerializer(wallets, many=True)
    return Response(serializer.data)