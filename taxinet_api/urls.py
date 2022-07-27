from django.urls import path

from . import views

urlpatterns = [
    # admin urls
    path("admin_get_all_requests", views.admin_get_all_requests),
    path("admin_request_detail/<str:slug>/", views.admin_ride_detail),
    path("admin_update_requested_ride/<str:slug>/", views.admin_update_requested_ride),
    path("admin_send_message/<str:slug>/", views.admin_send_message),
    path("admin_get_ride_messages/<str:slug>/", views.admin_get_ride_messages),
    path("admin_assign_request_to_driver/", views.admin_assign_request_to_driver),
    path("admin_bid_ride/<str:slug>/", views.admin_bid_ride),
    path("admin_add_to_completed_bid_on_rides/<str:slug>/", views.admin_add_to_completed_bid_on_rides),
    path("admin_get_all_drivers_inventories/", views.admin_get_all_drivers_inventories),
    path("admin_get_driver_inventory/<int:driver_id>/", views.admin_get_driver_inventory),
    # admin urls
    path('all_ride_requests/', views.get_all_requests),
    path('get_all_my_ride_requests/', views.get_all_my_ride_requests),
    path('ride_requests/<str:slug>/', views.ride_detail),
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

    #     drivers confirmed payments
    path('payment/new/', views.post_payment),
    path('get_drivers_payments/', views.get_all_driver_payments),

    #     drivers inventoryOptions
    path("get_driver_inventory/", views.get_driver_inventory),
    path("get_all_drivers_inventories/", views.get_all_drivers_inventories),
    path("add_drivers_inventories/", views.create_drivers_inventory),

    path('add_to_assigned_rejected/', views.add_to_assigned_rejected),
    path('get_all_rejected_assigned_ride/', views.get_all_rejected_assigned_ride),
    path('add_to_assigned_accepted/', views.add_to_assigned_accepted),
    path('get_all_accepted_assigned_ride/', views.get_all_accepted_assigned_ride),
    path('assign_to_driver/', views.assign_to_driver),
    path('get_all_assigned_ride/', views.get_all_assigned_ride),
    path('cancel_schedule/', views.cancel_schedule),
    path('get_all_cancelled_ride/', views.get_all_cancelled_ride),

    path("post_to_contact/", views.send_to_contact),
    path("get_all_contact_us_messages/", views.get_all_contact_us_messages),
]
