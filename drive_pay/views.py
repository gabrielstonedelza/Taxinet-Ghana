from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import permissions, generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import RequestDriveAndPay, AddToApprovedDriveAndPay, PayExtraForDriveAndPay,PayDailyForPayAndDrive
from .serializers import RequestDriveAndPaySerializer,AddToApprovedDriveAndPaySerializer, LockCarForTheDaySerializer,PayExtraForDriveAndPaySerializer, PayDailyForPayAndDriveSerializer
from car_sales.models import Vehicle
from datetime import datetime

# extra payment
@api_view(['GET','POST'])
@permission_classes([permissions.IsAuthenticated])
def add_to_drive_and_pay_daily(request):
    my_date = datetime.today()
    de_date = my_date.date()
    serializer = PayDailyForPayAndDriveSerializer(data=request.data)
    if serializer.is_valid():
        if not PayDailyForPayAndDrive.objects.filter(user=request.user).filter(
        month_paid=de_date.month).filter(year_paid=de_date.year).exists():
            serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_my_daily_payments_for_drive_and_pay(request):
    my_extra_payments = PayDailyForPayAndDrive.objects.filter(user=request.user).order_by('-date_paid')
    serializer = PayDailyForPayAndDriveSerializer(my_extra_payments, many=True)
    return Response(serializer.data)
# extra payment



@api_view(['GET','POST'])
@permission_classes([permissions.IsAuthenticated])
def add_to_drive_and_pay_complete(request,id):
    pay_drive = get_object_or_404(AddToApprovedDriveAndPay,id=id)
    serializer = AddToApprovedDriveAndPaySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(drive_and_pay=pay_drive)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_my_approved_drive_and_pay(request):
    my_approved = AddToApprovedDriveAndPay.objects.filter(user=request.user).filter(expired=False).order_by('-date_approved')
    serializer = AddToApprovedDriveAndPaySerializer(my_approved, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_approved_drive_and_pay(request):
    approved = AddToApprovedDriveAndPay.objects.filter(expired=False).order_by('-date_approved')
    serializer = AddToApprovedDriveAndPaySerializer(approved, many=True)
    return Response(serializer.data)


@api_view(['GET','POST'])
@permission_classes([permissions.IsAuthenticated])
def request_drive_and_pay(request,id):
    vehicle = get_object_or_404(Vehicle,id=id)
    serializer = RequestDriveAndPaySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user,car=vehicle)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_drive_and_pay_requests(request):
    my_requests = RequestDriveAndPay.objects.filter(user=request.user).filter(request_approved="Pending").order_by('-date_requested')
    serializer = RequestDriveAndPaySerializer(my_requests, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_drive_and_pay_requests(request):
    all_requests = RequestDriveAndPay.objects.all().order_by('-date_requested')
    serializer = RequestDriveAndPaySerializer(all_requests, many=True)
    return Response(serializer.data)


@api_view(['GET', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def delete_drive_and_pay(request, id):
    try:
        order = get_object_or_404(RequestDriveAndPay, id=id)
        order.delete()
    except RequestDriveAndPay.DoesNotExist:
        return Http404
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def lock_car(request):
    serializer = LockCarForTheDaySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_approve_drive_drive(request,pk):
    my_approved = get_object_or_404(AddToApprovedDriveAndPay,pk=pk)
    serializer = AddToApprovedDriveAndPaySerializer(my_approved, data=request.data)
    if serializer.is_valid():
        serializer.save(drive_and_pay=my_approved)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)