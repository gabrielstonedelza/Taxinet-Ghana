from django.shortcuts import get_object_or_404
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import (Complains,
                     DriversLocation, ConfirmDriverPayment, DriverVehicleInventory,
                     AcceptedScheduledRides, RejectedScheduledRides, BidScheduleRide, CompletedBidOnScheduledRide,
                     CompletedScheduledRides, ScheduledNotifications, Messages, ScheduleRide, AssignScheduleToDriver,
                     AcceptAssignedScheduled,
                     RejectAssignedScheduled, CancelScheduledRide)
from .serializers import (ComplainsSerializer,
                          ConfirmDriverPaymentSerializer, DriversLocationSerializer, ScheduleRideSerializer,
                          BidScheduleRideSerializer, AcceptedScheduledRidesSerializer, \
                          RejectedScheduledRidesSerializer, MessagesSerializer, DriverVehicleInventorySerializer,
                          CompletedScheduledRidesSerializer, \
                          CompletedBidOnScheduledRideSerializer, ScheduledNotificationSerializer,
                          CancelledScheduledRideSerializer, RejectScheduleToDriverSerializer,
                          AcceptScheduleToDriverSerializer, AssignScheduleToDriverSerializer)


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
        serializer.save(driver=request.user, )
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


# messages
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def send_message(request, ride_id):
    ride = get_object_or_404(ScheduleRide, id=ride_id)
    serializer = MessagesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user, ride=ride)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_driver_passenger_messages(request, ride_id):
    ride = get_object_or_404(ScheduleRide, id=ride_id)
    messages = Messages.objects.filter(ride=ride).order_by('date_sent')
    serializer = BidScheduleRideSerializer(messages, many=True)
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


# completed bid on rides
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def get_all_completed_bid_on_rides(request):
    completed_bid_rides = CompletedBidOnScheduledRide.objects.all().order_by('-date_completed')
    serializer = CompletedBidOnScheduledRideSerializer(completed_bid_rides, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def add_to_completed_bid_on_rides(request):
    serializer = CompletedBidOnScheduledRideSerializer(data=request.data)
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
@permission_classes([permissions.IsAuthenticated])
def ride_detail(request, ride_id):
    ride = get_object_or_404(ScheduleRide, id=ride_id)
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


# accept requested ride functions
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def bid_ride(request, ride_id):
    ride = get_object_or_404(ScheduleRide, id=ride_id)
    serializer = BidScheduleRideSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user, scheduled_ride=ride)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_bids(request, ride_id):
    ride = get_object_or_404(ScheduleRide, id=ride_id)
    bids = BidScheduleRide.objects.filter(scheduled_ride=ride).order_by('date_accepted')
    serializer = BidScheduleRideSerializer(bids, many=True)
    return Response(serializer.data)


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
    notifications = ScheduledNotifications.objects.filter(notification_to=request.user).order_by('-date_created')
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
