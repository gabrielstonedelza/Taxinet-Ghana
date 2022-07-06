from django.urls import path

from . import views

urlpatterns = [
    path('all_ride_requests/', views.get_all_requests),
    path('ride_requests/<int:ride_id>/', views.ride_detail),
    path('passengers_requests_completed/', views.get_passengers_requests_completed),
    path('drivers_requests_completed/', views.get_drivers_requests_completed),
    path('passengers_requests_uncompleted/', views.get_passengers_requests_uncompleted),
    path('drivers_requests_uncompleted/', views.get_drivers_requests_uncompleted),
    path('request_ride/new/', views.request_ride),
    path('bid_ride/<int:ride_id>/', views.bid_ride),
    path('send_message/<int:ride_id>/', views.send_message),
    path('all_bids/<int:ride_id>/', views.get_all_bids),
    path('all_driver_passenger_messages/<int:ride_id>/', views.get_driver_passenger_messages),
    path('update_requested_ride/<int:ride_id>/', views.update_requested_ride),
    path('delete_requested_ride/<int:ride_id>/', views.delete_requested_ride),
    path('get_all_rejected_rides/', views.get_all_rejected_rides),
    path('add_to_rejected_rides/', views.add_to_rejected_rides),
    path('get_all_accepted_rides/', views.get_all_accepted_rides),
    path('add_to_accepted_rides/', views.add_to_accepted_rides),
    path('announce_drivers_arrival/', views.announce_drivers_arrival),

    path('get_all_completed_rides/', views.get_all_completed_rides),
    path('add_to_completed_rides/', views.add_to_completed_rides),

    path('get_all_completed_bid_on_rides/', views.get_all_completed_bid_on_rides),
    path('add_to_completed_bid_on_rides/', views.add_to_completed_bid_on_rides),

    path('one_time_schedule/', views.get_scheduled_for_one_time),
    path('daily_schedules/', views.get_scheduled_for_daily),
    path('days_schedules/', views.get_scheduled_for_days),
    path('weekly_schedules/', views.get_scheduled_for_weekly),
    path('passengers_schedules/', views.get_scheduled_by_passenger),
    path('drivers_schedules/', views.get_scheduled_by_driver),

    #     notifications
    path('notifications/', views.get_all_user_notifications),
    path('user_notifications/', views.get_user_notifications),
    path('user_triggerd_notifications/', views.get_triggered_notifications),
    path('user_read_notifications/<int:id>/', views.read_notification),

    #     Complains
    path('complains/new/', views.post_complain),
    path('all_complains/', views.get_all_complains),
    path('user_complains/', views.user_complains),
    path('complain/<int:complain_id>/', views.get_detailed_complain),

    #     reviews
    path('drivers_reviews/', views.get_all_driver_reviews),
    path('passengers_reviews/', views.get_all_passenger_reviews),
    path('review/<int:review_id>/', views.review_detail),
    path('review/new/', views.post_review),

    #     drivers ratings
    path('drivers_ratings/', views.get_driver_ratings),
    path('passengers_ratings/', views.get_passenger_ratings),
    path('rating/new/', views.post_ratings),

    #     drivers confirmed payments
    path('payment/new/', views.post_payment),
    path('get_drivers_payments/', views.get_all_driver_payments),

    #     post and get searched_destinations
    path('destination/new/', views.add_to_searched_locations),
    path('get_destinations/', views.get_searched_locations),
]
