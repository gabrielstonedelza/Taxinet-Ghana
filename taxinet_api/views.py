from django.shortcuts import get_object_or_404
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import (RequestRide, BidRide, ScheduleRide, BidScheduleRide, Notifications, Complains, DriverReviews,
                     DriversLocation, DriversPoints, ConfirmDriverPayment, SearchedDestinations)
from .serializers import (RequestRideSerializer, BidRideSerializer, ScheduleRideSerializer, ComplainsSerializer,
                          BidScheduleRideSerializer, NotificationSerializer, DriverReviewSerializer,
                          RateDriverSerializer,
                          ConfirmDriverPaymentSerializer, DriversLocationSerializer, SearchDestinationsSerializer)


# get passengers searched locations
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def get_searched_locations(request):
    searched_destinations = SearchedDestinations.objects.filter(passenger=request.user).order_by('-date_searched')[:3]
    serializer = SearchDestinationsSerializer(searched_destinations, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def add_to_searched_locations(request):
    serializer = SearchDestinationsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(passenger=request.user)
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
    all_ride_requests = RequestRide.objects.all().order_by('-date_requested')
    serializer = RequestRideSerializer(all_ride_requests, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def ride_detail(request, ride_id):
    ride = get_object_or_404(RequestRide, id=ride_id)
    serializer = RequestRideSerializer(ride, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_passengers_requests_completed(request):
    passenger_requests = RequestRide.objects.filter(passenger=request.user).filter(completed=True).order_by(
        '-date_requested')
    serializer = RequestRideSerializer(passenger_requests, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_drivers_requests_completed(request):
    drivers_requests = RequestRide.objects.filter(driver=request.user).filter(completed=True).order_by(
        '-date_requested')
    serializer = RequestRideSerializer(drivers_requests, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_passengers_requests_uncompleted(request):
    passenger_requests = RequestRide.objects.filter(passenger=request.user).filter(completed=False).order_by(
        '-date_requested')
    serializer = RequestRideSerializer(passenger_requests, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_drivers_requests_uncompleted(request):
    drivers_requests = RequestRide.objects.filter(driver=request.user).filter(completed=False).order_by(
        '-date_requested')
    serializer = RequestRideSerializer(drivers_requests, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def request_ride(request):
    serializer = RequestRideSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(passenger=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_requested_ride(request, ride_id):
    ride = get_object_or_404(RequestRide, id=ride_id)
    serializer = RequestRideSerializer(ride, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# accept requested ride functions
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def bid_ride(request, ride_id):
    ride = get_object_or_404(RequestRide, id=ride_id)
    serializer = BidRideSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user, ride=ride)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_bid(request, bid_id):
    bid = get_object_or_404(BidRide, id=bid_id)
    serializer = BidRideSerializer(bid, data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_bids(request, ride_id):
    ride = get_object_or_404(RequestRide, id=ride_id)
    bids = BidRide.objects.filter(ride=ride).order_by('date_accepted')
    serializer = BidRideSerializer(bids, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_accepted_ride(request, ride_id, accept_id):
    ride = get_object_or_404(RequestRide, id=ride_id)
    accepted_id = get_object_or_404(BidRide, id=accept_id)
    serializer = BidRideSerializer(accepted_id, data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user, ride=ride)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def accepted_request_detail(request, accept_id):
    accepted_id = get_object_or_404(BidRide, id=accept_id)
    serializer = BidRideSerializer(accepted_id, many=False)
    return Response(serializer.data)


# scheduling ride
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def schedule_ride(request):
    serializer = ScheduleRideSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(passenger=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def bid_scheduled_ride(request, ride_id):
    ride = get_object_or_404(ScheduleRide, id=ride_id)
    serializer = BidScheduleRideSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user, scheduled_ride=ride)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_schedule_ride(request, ride_id):
    ride = get_object_or_404(ScheduleRide, id=ride_id)
    serializer = ScheduleRideSerializer(ride, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_scheduled(request):
    scheduled = ScheduleRide.objects.all().order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(scheduled, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def scheduled_ride_detail(request, scheduled_ride):
    scheduled_ride = get_object_or_404(ScheduleRide, id=scheduled_ride)
    serializer = ScheduleRideSerializer(scheduled_ride, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_scheduled_for_one_time(request):
    one_time_schedule = ScheduleRide.objects.filter(schedule_option="One Time").order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(one_time_schedule, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_scheduled_for_daily(request):
    daily_schedule = ScheduleRide.objects.filter(schedule_option="Daily").order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(daily_schedule, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_scheduled_for_days(request):
    days_schedule = ScheduleRide.objects.filter(schedule_option="Days").order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(days_schedule, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_scheduled_for_weekly(request):
    weekly_schedule = ScheduleRide.objects.filter(schedule_option="Weekly").order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(weekly_schedule, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_scheduled_for_monthly(request):
    monthly_schedule = ScheduleRide.objects.filter(schedule_option="Monthly").order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(monthly_schedule, many=True)
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


# accept schedule ride and bid

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def accept_schedule_ride(request, ride_id):
    ride = get_object_or_404(ScheduleRide, id=ride_id)
    serializer = BidScheduleRideSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user, ride=ride)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def accept_schedule_ride_detail(request, accept_id):
    accepted_id = get_object_or_404(BidScheduleRide, id=accept_id)
    serializer = BidScheduleRideSerializer(accepted_id, many=False)
    return Response(serializer.data)


# notifications
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_user_notifications(request):
    notifications = Notifications.objects.filter(notification_to=request.user).order_by('-date_created')
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_user_notifications(request):
    notifications = Notifications.objects.filter(notification_to=request.user).filter(read="Not Read").order_by(
        '-date_created')
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_triggered_notifications(request):
    notifications = Notifications.objects.filter(notification_to=request.user).filter(
        notification_trigger="Triggered").filter(
        read="Not Read").order_by('-date_created')
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated])
def read_notification(request, id):
    notification = get_object_or_404(Notifications, id=id)
    serializer = NotificationSerializer(notification, data=request.data)
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


# driver reviews
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_driver_reviews(request):
    reviews = DriverReviews.objects.filter(driver=request.user).order_by('-date_posted')
    serializer = DriverReviewSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_passenger_reviews(request):
    reviews = DriverReviews.objects.filter(passenger=request.user).order_by('-date_posted')
    serializer = DriverReviewSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def review_detail(request, review_id):
    review = get_object_or_404(DriverReviews, id=review_id)
    serializer = DriverReviewSerializer(review, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def post_review(request):
    serializer = DriverReviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(passenger=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# driver ratings
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_driver_ratings(request):
    ratings = DriversPoints.objects.filter(driver=request.user).order_by('-date_rated')
    serializer = RateDriverSerializer(ratings, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_passenger_ratings(request):
    ratings = DriversPoints.objects.filter(passenger=request.user).order_by('-date_rated')
    serializer = RateDriverSerializer(ratings, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def post_ratings(request):
    serializer = RateDriverSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(passenger=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
