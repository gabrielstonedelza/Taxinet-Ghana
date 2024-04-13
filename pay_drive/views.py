from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from cars_for_rent.models import CarsForRent
from .models import RequestPayAndDrive, AddToApprovedPayAndDrive, PayExtraDriveAndPay
from .serializers import RequestPayAndDriveSerializer, AddToApprovedPayAndDriveSerializer, PayExtraDriveAndPaySerializer


# payment daily
@api_view(['GET','POST'])
@permission_classes([permissions.IsAuthenticated])
def add_to_pay_and_drive_extra(request):
    serializer = PayExtraDriveAndPaySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_my_extra_payment_for_pay_and_drive(request):
    my_daily_payments = PayExtraDriveAndPay.objects.filter(user=request.user).order_by('-date_paid')
    serializer = PayExtraDriveAndPaySerializer(my_daily_payments, many=True)
    return Response(serializer.data)
# payment daily

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_my_approved_pay_and_drive(request):
    my_approved = AddToApprovedPayAndDrive.objects.filter(user=request.user).filter(expired=False).order_by('-date_approved')
    serializer = AddToApprovedPayAndDriveSerializer(my_approved, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_approved_pay_and_drive(request):
    approved = AddToApprovedPayAndDrive.objects.filter(expired=False).order_by('-date_approved')
    serializer = AddToApprovedPayAndDriveSerializer(approved, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def request_pay_and_drive(request,id):
    vehicle = get_object_or_404(CarsForRent, id=id)
    serializer = RequestPayAndDriveSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user,car=vehicle)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_pay_and_drive_requests(request):
    my_requests = RequestPayAndDrive.objects.filter(user=request.user).filter(request_approved="Pending").order_by('-date_requested')
    serializer = RequestPayAndDriveSerializer(my_requests, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_pay_and_drive_requests(request):
    all_requests = RequestPayAndDrive.objects.all().order_by('-date_requested')
    serializer = RequestPayAndDriveSerializer(all_requests, many=True)
    return Response(serializer.data)


@api_view(['GET', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def delete_pay_and_drive(request, id):
    try:
        order = get_object_or_404(RequestPayAndDrive, id=id)
        order.delete()
    except RequestPayAndDrive.DoesNotExist:
        return Http404
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_approve_pay_drive(request,pk):
    my_approved = get_object_or_404(AddToApprovedPayAndDrive,pk=pk)
    serializer = AddToApprovedPayAndDriveSerializer(my_approved, data=request.data)
    if serializer.is_valid():
        serializer.save(pay_and_drive=my_approved,user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# admin approve pay and drive request and add user to approved and confirmed requests

@api_view(['GET','POST'])
@permission_classes([permissions.IsAuthenticated])
def add_to_pay_and_drive_complete(request,id):
    pay_drive_request = get_object_or_404(RequestPayAndDrive,id=id)
    serializer = AddToApprovedPayAndDriveSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(pay_and_drive=pay_drive_request)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated])
def approve_pay_drive_request(request,pk):
    request_to_approve = get_object_or_404(RequestPayAndDrive,pk=pk)
    serializer = RequestPayAndDriveSerializer(request_to_approve, data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user,car=request_to_approve)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)