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
    path('update_bid/<int:bid_id>/', views.update_bid),
    path('all_bids/<int:ride_id>/', views.get_all_bids),
    path('accepted_ride/<int:accept_id>/update/', views.update_accepted_ride),
    path('update_requested_ride/<int:ride_id>/', views.update_requested_ride),
    path('delete_requested_ride/<int:ride_id>/', views.delete_requested_ride),
    path('accepted_ride_detail/<int:accept_id>/', views.accepted_request_detail),

    # post,get and update drivers location
    path("get_drivers_location/", views.get_drivers_current_location),
    path("drivers_location/new/", views.store_drivers_location),
    path("delete_drivers_locations/", views.delete_drivers_locations),

    #     scheduling rides
    path('scheduled_ride/new/', views.schedule_ride),
    path('bid_scheduled_ride/<int:ride_id>/', views.bid_scheduled_ride),
    path('update_schedule_ride/<int:ride_id>/', views.update_schedule_ride),
    path('all_scheduled_rides/', views.get_all_scheduled),
    path('scheduled_ride/<int:scheduled_ride>/', views.scheduled_ride_detail),
    path('one_time_schedule/', views.get_scheduled_for_one_time),
    path('daily_schedules/', views.get_scheduled_for_daily),
    path('days_schedules/', views.get_scheduled_for_days),
    path('weekly_schedules/', views.get_scheduled_for_weekly),
    path('monthly_schedules/', views.get_scheduled_for_monthly),
    path('passengers_schedules/', views.get_scheduled_by_passenger),
    path('drivers_schedules/', views.get_scheduled_by_driver),
    path('accept_schedules/<int:ride_id>/detail/', views.accept_schedule_ride_detail),

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
