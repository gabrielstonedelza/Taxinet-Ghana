from django.shortcuts import get_object_or_404
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers
from rest_framework.views import APIView
from datetime import datetime, date, time, timedelta

from taxinet_users.models import PassengerProfile
from .models import (Complains, AddToUpdatedWallets,
                     DriversLocation, ConfirmDriverPayment, DriverVehicleInventory,
                     AcceptedScheduledRides, RejectedScheduledRides,
                     CompletedScheduledRidesToday, ScheduledNotifications, ScheduleRide, AssignScheduleToDriver,
                     AcceptAssignedScheduled, ContactUs,
                     RejectAssignedScheduled, CancelScheduledRide, PassengersWallet, AskToLoadWallet, DriverStartTrip,
                     DriverEndTrip, DriverAlertArrival)
from .serializers import (ComplainsSerializer, ContactUsSerializer,
                          ConfirmDriverPaymentSerializer, DriversLocationSerializer, ScheduleRideSerializer,
                          AcceptedScheduledRidesSerializer, \
                          RejectedScheduledRidesSerializer, DriverVehicleInventorySerializer,
                          CompletedScheduledRidesSerializer, \
                          ScheduledNotificationSerializer,
                          CancelledScheduledRideSerializer, RejectScheduleToDriverSerializer,
                          AdminScheduleRideSerializer,
                          AcceptScheduleToDriverSerializer, AssignScheduleToDriverSerializer, PassengerWalletSerializer,
                          AskToLoadWalletSerializer, AddToUpdatedWalletsSerializer, DriverStartTripSerializer,
                          DriverEndTripSerializer, DriverAlertArrivalSerializer)
from django.http import Http404


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
def admin_ride_detail(request, slug):
    ride = get_object_or_404(ScheduleRide, slug=slug)
    if ride:
        ride.read = "Read"
        ride.save()
    serializer = ScheduleRideSerializer(ride, many=False)
    return Response(serializer.data)


@api_view(['GET', 'PUT'])
@permission_classes([permissions.AllowAny])
def admin_update_requested_ride(request, slug):
    ride = get_object_or_404(ScheduleRide, slug=slug)
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
def admin_get_scheduled_for_one_time(request):
    one_time_schedule = ScheduleRide.objects.filter(schedule_type="One Time").order_by('-date_scheduled')
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


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def get_all_drivers_inventories(request):
    inventories = DriverVehicleInventory.objects.all().order_by('-date_checked')
    serializer = DriverVehicleInventorySerializer(inventories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def get_driver_inventory(request, driver_id):
    driver_inventory = DriverVehicleInventory.objects.filter(driver=driver_id).order_by('-date_checked')
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
    completed_rides = CompletedScheduledRidesToday.objects.all().order_by('-date_completed')
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
def ride_detail(request, slug):
    ride = get_object_or_404(ScheduleRide, slug=slug)
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


@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated])
def read_notification(request, id):
    notification = get_object_or_404(ScheduledNotifications, id=id)
    serializer = ScheduledNotificationSerializer(notification, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
@api_view(['GET', 'POST'])
@permission_classes([permissions.IsAuthenticated])
def driver_start_trip(request, ride_id):
    ride = get_object_or_404(ScheduleRide, id=ride_id)
    serializer = DriverStartTripSerializer(ride, data=request.data)
    if serializer.is_valid():
        serializer.save(driver=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@permission_classes([permissions.IsAuthenticated])
def driver_end_trip(request, ride_id):
    ride = get_object_or_404(ScheduleRide, id=ride_id)
    serializer = DriverEndTripSerializer(ride, data=request.data)
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
def get_driver_scheduled_for_one_time(request):
    one_time_schedule = ScheduleRide.objects.filter(schedule_type="One Time").filter(
        assigned_driver=request.user).order_by('-date_scheduled')
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


# passenger notifications
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_passenger_notifications(request):
    notifications = ScheduledNotifications.objects.filter(notification_to_passenger=request.user).order_by(
        '-date_created')
    serializer = ScheduledNotificationSerializer(notifications, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_passenger_notifications(request):
    notifications = ScheduledNotifications.objects.filter(notification_to_passenger=request.user).filter(
        read="Not Read").order_by(
        '-date_created')
    serializer = ScheduledNotificationSerializer(notifications, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_passengers_triggered_notifications(request):
    notifications = ScheduledNotifications.objects.filter(notification_to_passenger=request.user).filter(
        notification_trigger="Triggered").filter(
        read="Not Read").order_by('-date_created')
    serializer = ScheduledNotificationSerializer(notifications, many=True)
    return Response(serializer.data)
