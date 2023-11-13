from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework import permissions, generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import Wallets,UpdatedWallets
from .serializers import WalletsSerializer,UpdatedWalletsSerializer



@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_all_wallets(request):
    wallets = Wallets.objects.exclude(user=1).order_by('-date_loaded')
    serializer = WalletsSerializer(wallets, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT'])
@permission_classes([permissions.AllowAny])
def update_wallet(request, id):
    wallet = get_object_or_404(Wallets, id=id)
    serializer = WalletsSerializer(wallet, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def add_to_updated_wallet(request, id):
    wallet = get_object_or_404(Wallets, id=id)
    serializer = UpdatedWalletsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(wallet=wallet)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_updated_wallet(request):
    wallet = UpdatedWallets.objects.filter(user=request.user).order_by('-date_updated')
    serializer = UpdatedWalletsSerializer(wallet, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_wallet(request):
    wallet = Wallets.objects.filter(user=request.user).order_by('-date_loaded')
    serializer = WalletsSerializer(wallet, many=True)
    return Response(serializer.data)



