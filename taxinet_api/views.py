from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers
from rest_framework.views import APIView
from datetime import datetime, date, time, timedelta
from rest_framework import filters
from .send_sms import send_sms

from taxinet_users.models import PassengerProfile, DriverProfile, InvestorsProfile, User, PromoterProfile
from taxinet_users.serializers import AdminPassengerProfileSerializer, InvestorsProfileSerializer, \
    DriverProfileSerializer, UsersSerializer, PassengerProfileSerializer, PromoterProfileSerializer
from .models import (Complains, AddToUpdatedWallets, DriversCommission, DriverRequestCommission,
                     DriversLocation, ConfirmDriverPayment, DriverVehicleInventory,
                     AcceptedScheduledRides, RejectedScheduledRides,
                     CompletedScheduledRides, ScheduledNotifications, ScheduleRide, AssignScheduleToDriver,
                     AcceptAssignedScheduled, ContactUs,
                     RejectAssignedScheduled, CancelScheduledRide, PassengersWallet, AskToLoadWallet, DriverStartTrip,
                     Wallets, RideMessages, ExpensesRequest,
                     RegisterVehicle, WorkAndPay, OtherWallet,
                     DriverEndTrip, DriverAlertArrival, DriversWallet, LoadWallet, UpdatedWallets,
                     DriverAddToUpdatedWallets, DriverAskToLoadWallet, AddToPaymentToday, PrivateUserMessage, Stocks,
                     WalletDeduction,
                     DriverTransferCommissionToWallet,
                     MonthlySalary, PayPromoterCommission,
                     AddToBlockList)
from .serializers import (ComplainsSerializer, ContactUsSerializer,
                          ConfirmDriverPaymentSerializer, DriversLocationSerializer, ScheduleRideSerializer,
                          RegisterVehicleSerializer, ExpensesRequestSerializer,
                          AcceptedScheduledRidesSerializer, \
                          RejectedScheduledRidesSerializer, DriverVehicleInventorySerializer,
                          CompletedScheduledRidesSerializer, \
                          ScheduledNotificationSerializer,
                          CancelledScheduledRideSerializer, RejectScheduleToDriverSerializer,
                          AdminScheduleRideSerializer,
                          AcceptScheduleToDriverSerializer, AssignScheduleToDriverSerializer, PassengerWalletSerializer,
                          AskToLoadWalletSerializer, AddToUpdatedWalletsSerializer, DriverStartTripSerializer,
                          DriverEndTripSerializer, DriverAlertArrivalSerializer, DriversWalletSerializer,
                          DriverAddToUpdatedWalletsSerializer, LoadWalletSerializer,
                          AddToPaymentTodaySerializer, WorkAndPaySerializer, OtherWalletSerializer, WalletsSerializer,
                          DriverTransferCommissionToWalletSerializer,
                          DriverRequestCommissionSerializer, WalletDeductionSerializer,
                          LoadWalletSerializer, UpdatedWalletsSerializer, RideMessagesSerializer,
                          PrivateUserMessageSerializer, AddToBlockListSerializer, StocksSerializer,
                          MonthlySalarySerializer, PayPromoterCommissionSerializer, DriversCommissionSerializer)
from django.http import Http404


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def admin_add_driver_to_work_and_pay(request):
    serializer = WorkAndPaySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_get_all_work_and_pay(request):
    vehicles = WorkAndPay.objects.all().order_by('-date_started')
    serializer = WorkAndPaySerializer(vehicles, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def work_and_pay_detail(request, id):
    wallet = get_object_or_404(WorkAndPay, id=id)
    serializer = WorkAndPaySerializer(wallet, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def admin_register_vehicle(request):
    serializer = RegisterVehicleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_get_all_registered_vehicles(request):
    vehicles = RegisterVehicle.objects.all().order_by('-date_registered')
    serializer = RegisterVehicleSerializer(vehicles, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT'])
@permission_classes([permissions.AllowAny])
def update_vehicle(request, id):
    vehicle = get_object_or_404(RegisterVehicle, id=id)
    serializer = RegisterVehicleSerializer(vehicle, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def vehicle_detail(request, id):
    vehicle = get_object_or_404(RegisterVehicle, id=id)
    serializer = RegisterVehicleSerializer(vehicle, many=False)
    return Response(serializer.data)


# admin gets,posts and updates


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def add_to_updated_wallets(request):
    serializer = AddToUpdatedWalletsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
@permission_classes([permissions.AllowAny])
def delete_assigned_driver(request, pk):
    try:
        assigned_driver = get_object_or_404(AssignScheduleToDriver, pk=pk)
        assigned_driver.delete()
    except ValueError:
        return Http404
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def admin_load_passengers_wallet(request):
    serializer = PassengerWalletSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_get_all_passengers_wallet(request):
    wallets = PassengersWallet.objects.all().order_by('-date_loaded')
    serializer = PassengerWalletSerializer(wallets, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def wallet_detail(request, id):
    wallet = get_object_or_404(PassengersWallet, id=id)
    serializer = PassengerWalletSerializer(wallet, many=False)
    return Response(serializer.data)


@api_view(['GET', 'PUT'])
@permission_classes([permissions.AllowAny])
def update_wallet(request, id):
    wallet = get_object_or_404(PassengersWallet, id=id)
    serializer = PassengerWalletSerializer(wallet, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_get_all_request_to_load_wallet(request):
    wallets = AskToLoadWallet.objects.all().order_by('-date_requested')
    serializer = AskToLoadWalletSerializer(wallets, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def load_wallet_detail(request, id):
    wallet = get_object_or_404(AskToLoadWallet, id=id)
    if wallet:
        wallet.read = "Read"
        wallet.save()
    serializer = AskToLoadWalletSerializer(wallet, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_get_all_user_notifications(request):
    notifications = ScheduledNotifications.objects.filter(notification_to=1).order_by('-date_created')[:6]
    serializer = ScheduledNotificationSerializer(notifications, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_get_five_requests(request):
    all_ride_requests = ScheduleRide.objects.all().order_by('date_scheduled')[:6]
    serializer = ScheduleRideSerializer(all_ride_requests, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_get_all_requests(request):
    all_ride_requests = ScheduleRide.objects.all().order_by('date_scheduled')
    serializer = ScheduleRideSerializer(all_ride_requests, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_get_all_requests_by_date(request, request_date):
    all_ride_requests = ScheduleRide.objects.filter(date_scheduled=request_date).order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(all_ride_requests, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_ride_detail(request, id):
    ride = get_object_or_404(ScheduleRide, id=id)
    if ride:
        ride.read = "Read"
        ride.save()
    serializer = ScheduleRideSerializer(ride, many=False)
    return Response(serializer.data)


@api_view(['GET', 'PUT'])
@permission_classes([permissions.AllowAny])
def admin_update_requested_ride(request, id):
    ride = get_object_or_404(ScheduleRide, id=id)
    serializer = AdminScheduleRideSerializer(ride, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def admin_assign_request_to_driver(request):
    serializer = AssignScheduleToDriverSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_get_all_assigned_drivers(request):
    all_assigned_drivers = AssignScheduleToDriver.objects.all().order_by('-date_assigned')
    serializer = AssignScheduleToDriverSerializer(all_assigned_drivers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_get_all_drivers_inventories(request):
    inventories = DriverVehicleInventory.objects.all().order_by('-date_checked')
    serializer = DriverVehicleInventorySerializer(inventories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_get_all_drivers_inventories_by_date(request, inventory_date):
    inventories = DriverVehicleInventory.objects.filter(date_checked=inventory_date).order_by('-date_checked')
    serializer = DriverVehicleInventorySerializer(inventories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_get_inventories_today(request):
    my_date_tim = datetime.now()
    inventories = DriverVehicleInventory.objects.filter(date_checked=my_date_tim.today()).filter(
        read="Not Read").order_by('date_checked')
    serializer = DriverVehicleInventorySerializer(inventories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_get_driver_inventory(request, driver_id):
    driver_inventory = DriverVehicleInventory.objects.filter(driver=driver_id).order_by('-date_checked')
    serializer = DriverVehicleInventorySerializer(driver_inventory, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_get_inventory_detail(request, id):
    driver_inventory = get_object_or_404(DriverVehicleInventory, id=id)
    if driver_inventory:
        driver_inventory.read = "Read"
        driver_inventory.checked_today = True
        driver_inventory.save()
    serializer = DriverVehicleInventorySerializer(driver_inventory, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_get_pending_schedules(request):
    pending = ScheduleRide.objects.filter(status="Pending").order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(pending, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_get_reviewing_schedules(request):
    reviewing = ScheduleRide.objects.filter(status="Reviewing").order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(reviewing, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_get_active_schedules(request):
    active = ScheduleRide.objects.filter(status="Active").order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(active, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_get_cancelled_schedules(request):
    cancelled = ScheduleRide.objects.filter(status="Cancelled").order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(cancelled, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_get_scheduled_for_short_trips(request):
    one_time_schedule = ScheduleRide.objects.filter(schedule_type="Short Trip").order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(one_time_schedule, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_get_scheduled_for_daily(request):
    daily_schedule = ScheduleRide.objects.filter(schedule_type="Daily").order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(daily_schedule, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_get_scheduled_for_days(request):
    days_schedule = ScheduleRide.objects.filter(schedule_type="Days").order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(days_schedule, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_get_scheduled_for_weekly(request):
    weekly_schedule = ScheduleRide.objects.filter(schedule_type="Weekly").order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(weekly_schedule, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_get_scheduled_for_monthly(request):
    weekly_schedule = ScheduleRide.objects.filter(schedule_type="Monthly").order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(weekly_schedule, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# admin gets,posts and updates

# @api_view(['GET'])
# @permission_classes([permissions.IsAuthenticated])
# def get_my_wallet(request):
#     wallet = PassengersWallet.objects.filter(passengers=request.user).order_by('-date_loaded')
#     serializer = PassengerWalletSerializer(wallet, many=True)
#     return Response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def request_to_load_wallet(request):
    serializer = AskToLoadWalletSerializer(data=request.data)
    user = get_object_or_404(PassengerProfile, user=request.user)
    if serializer.is_valid():
        serializer.save(passenger=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def send_to_contact(request):
    serializer = ContactUsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_all_contact_us_messages(request):
    messages = ContactUs.objects.all().order_by('-date_sent')
    serializer = ContactUsSerializer(messages, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def add_to_assigned_rejected(request):
    serializer = RejectScheduleToDriverSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(driver=request.user, )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def get_all_rejected_assigned_ride(request):
    rejected_assigns = RejectAssignedScheduled.objects.all().order_by('-date_rejected')
    serializer = RejectScheduleToDriverSerializer(rejected_assigns, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def add_to_assigned_accepted(request):
    serializer = AcceptScheduleToDriverSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(driver=request.user, )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def get_all_accepted_assigned_ride(request):
    accepted_assigns = AcceptAssignedScheduled.objects.all().order_by('-date_accepted')
    serializer = AcceptScheduleToDriverSerializer(accepted_assigns, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def assign_to_driver(request):
    serializer = AssignScheduleToDriverSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def get_all_assigned_ride(request):
    assigns = AssignScheduleToDriver.objects.all().order_by('-date_assigned')
    serializer = AssignScheduleToDriverSerializer(assigns, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def cancel_schedule(request):
    serializer = CancelledScheduledRideSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(passenger=request.user, )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def get_all_cancelled_ride(request):
    cancelled = CancelScheduledRide.objects.all().order_by('-date_cancelled')
    serializer = CancelledScheduledRideSerializer(cancelled, many=True)
    return Response(serializer.data)


# drivers inventories
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def drivers_inventory_detail(request, id):
    inventory = get_object_or_404(DriverVehicleInventory, id=id)
    serializer = DriverVehicleInventorySerializer(inventory, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_drivers_inventories(request):
    inventories = DriverVehicleInventory.objects.all().order_by('-date_checked')
    serializer = DriverVehicleInventorySerializer(inventories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_driver_inventory(request):
    driver_inventory = DriverVehicleInventory.objects.filter(driver=request.user).order_by('-date_checked')
    serializer = DriverVehicleInventorySerializer(driver_inventory, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def create_drivers_inventory(request, ):
    serializer = DriverVehicleInventorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(driver=request.user, )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def get_driver_location(request, driver_id):
    driver_location = DriversLocation.objects.filter(driver=driver_id).order_by('-date_updated')[:1]
    serializer = DriversLocationSerializer(driver_location, many=True)
    return Response(serializer.data)


# completed rides
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def get_all_completed_rides(request):
    completed_rides = CompletedScheduledRides.objects.all().order_by('-date_completed')
    serializer = CompletedScheduledRidesSerializer(completed_rides, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def add_to_completed_rides(request):
    serializer = CompletedScheduledRidesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(driver=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# accepted rides
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def get_all_accepted_rides(request):
    accepted_rides = AcceptedScheduledRides.objects.all().order_by('-date_accepted')
    serializer = AcceptedScheduledRidesSerializer(accepted_rides, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def add_to_accepted_rides(request):
    serializer = AcceptedScheduledRidesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(driver=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# rejected rides in
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def get_all_rejected_rides(request):
    rejected_rides = RejectedScheduledRides.objects.all().order_by('-date_rejected')
    serializer = RejectedScheduledRidesSerializer(rejected_rides, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def add_to_rejected_rides(request):
    serializer = RejectedScheduledRidesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(driver=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# get and store drivers current location
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def get_drivers_current_location(request):
    location = DriversLocation.objects.all().order_by('-date_updated')
    serializer = DriversLocationSerializer(location, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def store_drivers_location(request):
    serializer = DriversLocationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(driver=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def delete_drivers_locations(request):
    try:
        all_drivers_locations = DriversLocation.objects.all().order_by('-date_updated')
        for i in all_drivers_locations:
            i.delete()
    except DriversLocation.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_204_NO_CONTENT)


# get all requests
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def get_all_requests(request):
    all_ride_requests = ScheduleRide.objects.all().order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(all_ride_requests, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def get_all_my_ride_requests(request):
    all_ride_requests = ScheduleRide.objects.filter(passenger=request.user).order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(all_ride_requests, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def ride_detail(request, id):
    ride = get_object_or_404(ScheduleRide, id=id)
    serializer = ScheduleRideSerializer(ride, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_passengers_requests_completed(request):
    passenger_requests = ScheduleRide.objects.filter(passenger=request.user).filter(completed=True).order_by(
        '-date_scheduled')
    serializer = ScheduleRideSerializer(passenger_requests, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_drivers_requests_completed(request):
    drivers_requests = ScheduleRide.objects.filter(driver=request.user).filter(completed=True).order_by(
        '-date_scheduled')
    serializer = ScheduleRideSerializer(drivers_requests, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_passengers_requests_uncompleted(request):
    passenger_requests = ScheduleRide.objects.filter(passenger=request.user).filter(completed=False).order_by(
        '-date_scheduled')
    serializer = ScheduleRideSerializer(passenger_requests, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_drivers_requests_uncompleted(request):
    drivers_requests = ScheduleRide.objects.filter(driver=request.user).filter(completed=False).order_by(
        '-date_scheduled')
    serializer = ScheduleRideSerializer(drivers_requests, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def request_ride(request):
    serializer = ScheduleRideSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(passenger=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_requested_ride(request, ride_id):
    ride = get_object_or_404(ScheduleRide, id=ride_id)
    serializer = ScheduleRideSerializer(ride, data=request.data)
    if serializer.is_valid():
        serializer.save(passenger=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def delete_requested_ride(request, ride_id):
    try:
        ride = get_object_or_404(ScheduleRide, id=ride_id)
        ride.delete()
    except ScheduleRide.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_scheduled_for_one_time(request):
    one_time_schedule = ScheduleRide.objects.filter(schedule_type="One Time").order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(one_time_schedule, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_scheduled_for_daily(request):
    daily_schedule = ScheduleRide.objects.filter(schedule_type="Daily").order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(daily_schedule, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_scheduled_for_days(request):
    days_schedule = ScheduleRide.objects.filter(schedule_type="Days").order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(days_schedule, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_scheduled_for_weekly(request):
    weekly_schedule = ScheduleRide.objects.filter(schedule_type="Weekly").order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(weekly_schedule, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_scheduled_by_passenger(request):
    scheduled_ride = ScheduleRide.objects.filter(passenger=request.user).order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(scheduled_ride, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_scheduled_by_driver(request):
    scheduled_ride = ScheduleRide.objects.filter(driver=request.user).order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(scheduled_ride, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# notifications
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_user_notifications(request):
    notifications = ScheduledNotifications.objects.filter(notification_to_passenger=request.user).order_by(
        '-date_created')
    serializer = ScheduledNotificationSerializer(notifications, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_driver_notifications(request):
    notifications = ScheduledNotifications.objects.filter(notification_to=request.user).order_by(
        '-date_created')
    serializer = ScheduledNotificationSerializer(notifications, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_user_notifications(request):
    notifications = ScheduledNotifications.objects.filter(notification_to=request.user).filter(
        read="Not Read").order_by(
        '-date_created')
    serializer = ScheduledNotificationSerializer(notifications, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_triggered_notifications(request):
    notifications = ScheduledNotifications.objects.filter(notification_to=request.user).filter(
        notification_trigger="Triggered").filter(
        read="Not Read").order_by('-date_created')
    serializer = ScheduledNotificationSerializer(notifications, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def read_notification(request):
    notifications = ScheduledNotifications.objects.filter(notification_to=request.user).filter(
        read="Not Read").order_by('-date_created')
    for i in notifications:
        i.read = "Read"
        i.save()

    serializer = ScheduledNotificationSerializer(notifications, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def notification_detail(request, id):
    notification = get_object_or_404(ScheduledNotifications, id=id)
    serializer = ScheduledNotificationSerializer(notification, many=False)
    return Response(serializer.data)


# Complains
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def post_complain(request):
    serializer = ComplainsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(complainant=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_complains(request):
    complains = Complains.objects.all().order_by('-date_posted')
    serializer = ComplainsSerializer(complains, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def user_complains(request):
    u_complains = Complains.objects.filter(complainant=request.user).order_by('-date_posted')
    serializer = ComplainsSerializer(u_complains, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_detailed_complain(request, complain_id):
    complain = get_object_or_404(Complains, id=complain_id)
    serializer = ComplainsSerializer(complain, many=False)
    return Response(serializer.data)


# confirm driver payment
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def post_payment(request):
    serializer = ConfirmDriverPaymentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(driver=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_driver_payments(request):
    payments = ConfirmDriverPayment.objects.filter(driver=request.user).order_by('-date_confirmed')
    serializer = ConfirmDriverPaymentSerializer(payments, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_wallet(request):
    wallet = PassengersWallet.objects.filter(passenger=request.user).order_by('-date_loaded')
    serializer = PassengerWalletSerializer(wallet, many=True)
    return Response(serializer.data)


# passengers schedules categorized
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_active_schedules(request):
    active_schedule = ScheduleRide.objects.filter(passenger=request.user).filter(status="Active").order_by(
        '-date_scheduled')
    serializer = ScheduleRideSerializer(active_schedule, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_drives_assigned_schedules(request):
    assigned_schedules = ScheduleRide.objects.filter(assigned_driver=request.user).order_by(
        '-date_scheduled')
    serializer = ScheduleRideSerializer(assigned_schedules, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_drives_assigned_and_active_schedules(request):
    assigned_schedules = ScheduleRide.objects.filter(assigned_driver=request.user).filter(status="Active").order_by(
        '-date_scheduled')
    serializer = ScheduleRideSerializer(assigned_schedules, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# start and end trip
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def driver_start_trip(request):
    serializer = DriverStartTripSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(driver=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def driver_end_trip(request):
    serializer = DriverEndTripSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(driver=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def driver_alert_passenger(request):
    serializer = DriverAlertArrivalSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(driver=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# get schedule types and driver
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_driver_scheduled_for_short_trip(request):
    one_time_schedule = ScheduleRide.objects.filter(schedule_type="Short Trip").filter(
        assigned_driver=request.user).filter(completed=False).order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(one_time_schedule, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_driver_scheduled_for_daily(request):
    daily_schedule = ScheduleRide.objects.filter(schedule_type="Daily").filter(assigned_driver=request.user).order_by(
        '-date_scheduled')
    serializer = ScheduleRideSerializer(daily_schedule, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_driver_scheduled_for_days(request):
    days_schedule = ScheduleRide.objects.filter(schedule_type="Days").filter(assigned_driver=request.user).order_by(
        '-date_scheduled')
    serializer = ScheduleRideSerializer(days_schedule, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_driver_scheduled_for_weekly(request):
    weekly_schedule = ScheduleRide.objects.filter(schedule_type="Weekly").filter(assigned_driver=request.user).order_by(
        '-date_scheduled')
    serializer = ScheduleRideSerializer(weekly_schedule, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_driver_scheduled_for_monthly(request):
    weekly_schedule = ScheduleRide.objects.filter(schedule_type="Monthly").filter(
        assigned_driver=request.user).order_by(
        '-date_scheduled')
    serializer = ScheduleRideSerializer(weekly_schedule, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# passenger notifications
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_passenger_notifications(request):
    notifications = ScheduledNotifications.objects.filter(notification_to=request.user).order_by(
        '-date_created')
    serializer = ScheduledNotificationSerializer(notifications, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_passenger_notifications(request):
    notifications = ScheduledNotifications.objects.filter(notification_to=request.user).filter(
        read="Not Read").order_by(
        '-date_created')
    serializer = ScheduledNotificationSerializer(notifications, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_passengers_triggered_notifications(request):
    notifications = ScheduledNotifications.objects.filter(notification_to=request.user).filter(
        notification_trigger="Triggered").filter(
        read="Not Read").order_by('-date_created')
    serializer = ScheduledNotificationSerializer(notifications, many=True)
    return Response(serializer.data)


# drivers wallet
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def add_to_drivers_updated_wallets(request):
    serializer = DriverAddToUpdatedWalletsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def admin_load_drivers_wallet(request):
    serializer = DriversWalletSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_get_all_drivers_wallet(request):
    wallets = DriversWallet.objects.all().order_by('-date_loaded')
    serializer = DriversWalletSerializer(wallets, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def drivers_wallet_detail(request, id):
    wallet = get_object_or_404(DriversWallet, id=id)
    serializer = DriversWalletSerializer(wallet, many=False)
    return Response(serializer.data)


@api_view(['GET', 'PUT'])
@permission_classes([permissions.AllowAny])
def update_drivers_wallet(request, id):
    wallet = get_object_or_404(DriversWallet, id=id)
    serializer = DriversWalletSerializer(wallet, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_get_all_drivers_request_to_load_wallet(request):
    wallets = DriverAskToLoadWallet.objects.all().order_by('-date_requested')
    serializer = LoadWalletSerializer(wallets, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def load_drivers_wallet_detail(request, id):
    wallet = get_object_or_404(DriverAskToLoadWallet, id=id)
    if wallet:
        wallet.read = "Read"
        wallet.save()
    serializer = LoadWalletSerializer(wallet, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_drivers_wallet(request):
    wallet = DriversWallet.objects.filter(driver=request.user).order_by('-date_loaded')
    serializer = DriversWalletSerializer(wallet, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_get_scheduled_for_monthly(request):
    weekly_schedule = ScheduleRide.objects.filter(schedule_type="Monthly").order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(weekly_schedule, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def request_to_load_drivers_wallet(request):
    serializer = LoadWalletSerializer(data=request.data)
    user = get_object_or_404(DriverProfile, user=request.user)
    if serializer.is_valid():
        serializer.save(driver=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# drivers payments todays
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def add_to_drivers_payment_today(request):
    serializer = AddToPaymentTodaySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(driver=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_all_payments_today(request):
    payments = AddToPaymentToday.objects.all().order_by('-date_paid')
    serializer = AddToPaymentTodaySerializer(payments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_payments_today(request):
    my_date = datetime.today()
    payments = AddToPaymentToday.objects.filter(date_paid=my_date.date()).order_by('-date_paid')
    serializer = AddToPaymentTodaySerializer(payments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_get_all_drivers_payments_by_date(request, payment_date):
    payments = AddToPaymentToday.objects.filter(date_paid=payment_date).order_by('-date_paid')
    serializer = AddToPaymentTodaySerializer(payments, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_get_payment_detail(request, id):
    payment = get_object_or_404(AddToPaymentToday, id=id)
    if payment:
        payment.read = "Read"
        payment.save()
    serializer = AddToPaymentTodaySerializer(payment, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_work_and_pay(request):
    work_and_pay = WorkAndPay.objects.filter(driver=request.user).order_by('-date_started')
    serializer = WorkAndPaySerializer(work_and_pay, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_work_and_pay_detail(request, id):
    wallet = get_object_or_404(WorkAndPay, id=id)
    serializer = WorkAndPaySerializer(wallet, many=False)
    return Response(serializer.data)


# wallet transfer
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def transfer_to_wallet(request):
    serializer = OtherWalletSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(sender=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_wallet_transfers(request):
    transfers = OtherWallet.objects.filter(driver=request.user).order_by('-date_transferred')
    serializer = OtherWalletSerializer(transfers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def wallet_transfer_detail(request, id):
    transfer = get_object_or_404(OtherWallet, id=id)
    serializer = OtherWalletSerializer(transfer, many=False)
    return Response(serializer.data)


# update drivers wallet by username
@api_view(['GET', 'PUT'])
@permission_classes([permissions.AllowAny])
def update_drivers_wallet_with_username(request, user):
    wallet = get_object_or_404(DriversWallet, driver=user)
    serializer = DriversWalletSerializer(wallet, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
@permission_classes([permissions.AllowAny])
def update_passengers_wallet(request, user):
    wallet = get_object_or_404(PassengersWallet, passenger=user)
    serializer = PassengerWalletSerializer(wallet, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# get drivers payment and details
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def payments_today(request):
    payments = AddToPaymentToday.objects.all().order_by('-date_paid')
    serializer = AddToPaymentTodaySerializer(payments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def payment_detail(request, id):
    payment = get_object_or_404(AddToPaymentToday, id=id)
    serializer = RegisterVehicleSerializer(payment, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


# new wallet system
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def admin_load_users_wallet(request):
    serializer = WalletsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_get_all_users_wallet(request):
    wallets = Wallets.objects.exclude(user=1).order_by('-date_loaded')
    serializer = WalletsSerializer(wallets, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def user_wallet_detail(request, id):
    wallet = get_object_or_404(Wallets, id=id)
    serializer = WalletsSerializer(wallet, many=False)
    return Response(serializer.data)


@api_view(['GET', 'PUT'])
@permission_classes([permissions.AllowAny])
def admin_update_wallet(request, id):
    wallet = get_object_or_404(Wallets, id=id)
    serializer = WalletsSerializer(wallet, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_get_load_wallet_requests_detail(request, id):
    wallet = get_object_or_404(LoadWallet, id=id)
    if wallet:
        wallet.read = "Read"
        wallet.save()
    serializer = LoadWalletSerializer(wallet, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_all_request_to_load_wallet(request):
    wallets = LoadWallet.objects.all().order_by('-date_requested')
    serializer = LoadWalletSerializer(wallets, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def admin_add_to_updated_wallets(request):
    serializer = UpdatedWalletsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def user_request_to_load_wallet(request):
    serializer = LoadWalletSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_user_wallet(request):
    wallet = Wallets.objects.filter(user=request.user).order_by('-date_loaded')
    serializer = WalletsSerializer(wallet, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated])
def user_update_wallet(request, user):
    wallet = get_object_or_404(Wallets, user=user)
    serializer = WalletsSerializer(wallet, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# get wallet by user
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_wallet_by_user(request, user_id):
    wallet = get_object_or_404(Wallets, user=user_id)
    serializer = WalletsSerializer(wallet, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_wallet_by_username(request, username):
    wallet = get_object_or_404(Wallets, username=username)
    serializer = WalletsSerializer(wallet, many=False)
    return Response(serializer.data)


# ride messages
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def send_message(request, id):
    ride = get_object_or_404(ScheduleRide, id=id)
    serializer = RideMessagesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(ride=ride)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_ride_messages(request, id):
    messages = RideMessages.objects.filter(ride=id).order_by('-date_sent')
    serializer = RideMessagesSerializer(messages, many=True)
    return Response(serializer.data)


# expenses
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def add_expenses(request):
    serializer = ExpensesRequestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_all_expenses(request):
    vehicles = ExpensesRequest.objects.all().order_by('-date_requested')
    serializer = ExpensesRequestSerializer(vehicles, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def expense_detail(request, id):
    expense = get_object_or_404(ExpensesRequest, id=id)
    serializer = ExpensesRequestSerializer(expense, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_expenses_today(request):
    my_date = datetime.today()
    expenses = ExpensesRequest.objects.filter(date_requested=my_date.date()).order_by('-date_requested')
    serializer = ExpensesRequestSerializer(expenses, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_expenses_get_by_date(request, expense_date):
    payments = ExpensesRequest.objects.filter(date_requested=expense_date).order_by('-date_requested')
    serializer = ExpensesRequestSerializer(payments, many=True)
    return Response(serializer.data)


# searches
class SearchWallet(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Wallets.objects.all()
    serializer_class = WalletsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'phone']


class SearchScheduleRequest(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = ScheduleRide.objects.all()
    serializer_class = ScheduleRideSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['passenger_username', 'passenger_phone', 'driver_username', 'driver_phone', 'schedule_title']


class SearchDriver(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = DriverProfile.objects.all()
    serializer_class = DriverProfileSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'phone']


class SearchPassenger(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = PassengerProfile.objects.all()
    serializer_class = PassengerProfileSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'phone']


class SearchInvestor(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = InvestorsProfile.objects.all()
    serializer_class = InvestorsProfileSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'phone']


class SearchPayments(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = AddToPaymentToday.objects.all()
    serializer_class = AddToPaymentTodaySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'phone']


class SearchPromoter(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = PromoterProfile.objects.all()
    serializer_class = PromoterProfileSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'phone']


# new updates
@api_view(['GET', 'DELETE'])
@permission_classes([permissions.AllowAny])
def user_delete(request, pk):
    try:
        user = User.objects.get(pk=pk)
        user.delete()
    except User.DoesNotExist:
        return Http404
    return Response(status=status.HTTP_204_NO_CONTENT)


# private messages
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def send_private_message(request):
    serializer = PrivateUserMessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_private_message(request, user1, user2):
    all_messages = []
    messages1 = PrivateUserMessage.objects.filter(sender=user1, receiver=user2).order_by('-timestamp')
    messages2 = PrivateUserMessage.objects.filter(sender=user2, receiver=user1).order_by('-timestamp')
    for i in messages1:
        all_messages.append(i)
    for m in messages2:
        all_messages.append(m)
    serializer = PrivateUserMessageSerializer(all_messages, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def private_message_detail(request, user1, user2):
    message = PrivateUserMessage.objects.get(sender=user1, receiver=user2)
    if message:
        message.read = True
        message.save()
    serializer = PrivateUserMessageSerializer(message, many=False)
    return Response(serializer.data)


# block list
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def add_to_blocked(request):
    serializer = AddToBlockListSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
@permission_classes([permissions.AllowAny])
def remove_from_blocked(request, id):
    try:
        user_blocked = get_object_or_404(AddToBlockList, id=id)
        user_blocked.delete()
    except User.DoesNotExist:
        return Http404
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_blocked_users(request):
    users = AddToBlockList.objects.all().order_by('-date_blocked')
    serializer = AddToBlockListSerializer(users, many=True)
    return Response(serializer.data)


# promoter commission
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def add_promoter_commission(request):
    serializer = PayPromoterCommissionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_promoter_commissions(request):
    users = PayPromoterCommission.objects.all().order_by('-date_paid')
    serializer = PayPromoterCommissionSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_promoter_commission(request):
    users = PayPromoterCommission.objects.filter(promoter=request.user).order_by('-date_paid')
    serializer = PayPromoterCommissionSerializer(users, many=True)
    return Response(serializer.data)


# monthly salary
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def add_monthly_salary(request):
    serializer = MonthlySalarySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_monthly_salaries(request):
    users = MonthlySalary.objects.all().order_by('-date_paid')
    serializer = MonthlySalarySerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_salary(request):
    users = MonthlySalary.objects.filter(driver=request.user).order_by('-date_paid')
    serializer = MonthlySalarySerializer(users, many=True)
    return Response(serializer.data)


# stocks
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def add_stock(request):
    serializer = StocksSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_all_stocks(request):
    users = Stocks.objects.all().order_by('-date_added')
    serializer = StocksSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_passengers_requests(request, passenger):
    requests = ScheduleRide.objects.filter(passenger=passenger).order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(requests, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_stock(request, id):
    stock = get_object_or_404(Stocks, id=id)
    serializer = StocksSerializer(stock, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# drivers commission,
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def add_driver_commission(request):
    serializer = DriversCommissionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_drivers_commissions(request):
    users = MonthlySalary.objects.all().order_by('-date_paid')
    serializer = DriversCommissionSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_commission(request):
    users = DriversCommission.objects.filter(driver=request.user).order_by('-date_paid')
    serializer = DriversCommissionSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def driver_request_commission(request):
    serializer = DriverRequestCommissionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_drivers_commissions_requests(request):
    users = DriverRequestCommission.objects.all().order_by('-date_requested')
    serializer = DriverRequestCommissionSerializer(users, many=True)
    return Response(serializer.data)


# commission to wallet
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def driver_commission_to_wallet(request):
    serializer = DriverTransferCommissionToWalletSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# update commission
@api_view(['GET', 'DELETE'])
@permission_classes([permissions.AllowAny])
def user_commissions_delete(request, driver):
    try:
        commissions = DriversCommission.objects.filter(driver=driver)
        for i in commissions:
            i.delete()
    except User.DoesNotExist:
        return Http404
    return Response(status=status.HTTP_204_NO_CONTENT)


# wallet deduction
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def deduct_wallet(request):
    serializer = WalletDeductionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# async def job_monitor():
#     while True:
#         print('Check triggered jobs on the cluster')
#         send_sms("TG0VqHEFA9ZoqNtnw43GdVkKnBSBIpf2", "233593380008", "Hello Gabriel", "Taxinet")
#         await asyncio.sleep(10)
# loop = asyncio.get_event_loop()
# task = loop.create_task(job_monitor())
#
# try:
#     loop.run_until_complete(task)
# except asyncio.CancelledError:
#     pass

import pytz

current_time = datetime.now(pytz.timezone('Africa/Accra'))
drivers_numbers = ["0547236997", "0245086675", "0509556768", "0246873879", "0244858459", "0551300168", "0243143292",
                   "0244710522", "0596842925"]
drivers_tracking_numbers = ["0594095982", "0594097253", "0594163113", "0594143106", "0594140062", "0594162360",
                            "0594173115", "0594140058", "0594072852"]

if current_time.hour == 23:
    for i in drivers_numbers:
        send_sms("TG0VqHEFA9ZoqNtnw43GdVkKnBSBIpf2", i, "Attention!,please be advised, your car will be locked in one hour time,thank you.", "0244529353")


if current_time.hour == 00:
    for i in drivers_tracking_numbers:
        send_sms("TG0VqHEFA9ZoqNtnw43GdVkKnBSBIpf2", i, "relay,1#", "0244529353")
