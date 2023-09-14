from django.urls import path

from . import views

urlpatterns = [

    # vehicles
    path("vehicle_detail/<int:id>/", views.get_vehicle_detail),
    path("vehicle_update/<int:id>/", views.update_vehicle),
    path("all_vehicles/", views.get_all_registered_vehicles),

    path("admin_get_all_requests/", views.admin_get_all_requests),
    path("admin_get_all_requests_by_date/<str:request_date>/", views.admin_get_all_requests_by_date),
    path("admin_get_five_requests/", views.admin_get_five_requests),
    path("admin_request_detail/<str:id>/", views.admin_ride_detail),
    path("admin_update_requested_ride/<int:id>/", views.admin_update_requested_ride),

    path("admin_get_pending_schedules/", views.admin_get_pending_schedules),
    path("admin_get_reviewing_schedules/", views.admin_get_reviewing_schedules),
    path("admin_get_active_schedules/", views.admin_get_active_schedules),
    path("admin_get_cancelled_schedules/", views.admin_get_cancelled_schedules),
    path("admin_get_scheduled_for_weekly/", views.admin_get_scheduled_for_weekly),
    path("admin_get_scheduled_for_days/", views.admin_get_scheduled_for_days),
    path("admin_get_scheduled_for_daily/", views.admin_get_scheduled_for_daily),
    path("admin_get_scheduled_for_short_trips/", views.admin_get_scheduled_for_short_trips),
    path("admin_get_all_user_notifications/", views.admin_get_all_user_notifications),

    # admin urls
    path('all_ride_requests/', views.get_all_requests),
    path('get_all_my_ride_requests/', views.get_all_my_ride_requests),
    path('ride_requests/<int:id>/', views.ride_detail),
    path('passengers_requests_completed/', views.get_passengers_requests_completed),
    path('drivers_requests_completed/', views.get_drivers_requests_completed),
    path('passengers_requests_uncompleted/', views.get_passengers_requests_uncompleted),
    path('drivers_requests_uncompleted/', views.get_drivers_requests_uncompleted),
    path('request_ride/new/', views.request_ride),
    path('update_requested_ride/<int:ride_id>/', views.update_requested_ride),
    path('delete_requested_ride/<int:ride_id>/', views.delete_requested_ride),


    path('one_time_schedule/', views.get_scheduled_for_one_time),
    path('daily_schedules/', views.get_scheduled_for_daily),
    path('days_schedules/', views.get_scheduled_for_days),
    path('weekly_schedules/', views.get_scheduled_for_weekly),
    path('passengers_schedules/', views.get_scheduled_by_passenger),
    path('drivers_schedules/', views.get_scheduled_by_driver),

    #     Complains
    path('complains/new/', views.post_complain),
    path('all_complains/', views.get_all_complains),
    path('user_complains/', views.user_complains),
    path('complain/<int:complain_id>/', views.get_detailed_complain),

    #     drivers confirmed payment
    path('cancel_schedule/', views.cancel_schedule),
    path('get_all_cancelled_ride/', views.get_all_cancelled_ride),

    path("post_to_contact/", views.send_to_contact),
    path("get_all_contact_us_messages/", views.get_all_contact_us_messages),

    #     passengers schedules
    path("get_my_active_schedules/", views.get_my_active_schedules),

    #
    path("get_drives_assigned_schedules/", views.get_drives_assigned_schedules),
    path("get_drives_assigned_and_active_schedules/", views.get_drives_assigned_and_active_schedules),

    #     driver get schedule types
    path('get_driver_scheduled_for_short_trip/', views.get_driver_scheduled_for_short_trip),
    path('get_driver_scheduled_for_daily/', views.get_driver_scheduled_for_daily),
    path('get_driver_scheduled_for_days/', views.get_driver_scheduled_for_days),
    path('get_driver_scheduled_for_weekly/', views.get_driver_scheduled_for_weekly),
    path('get_driver_scheduled_for_monthly/', views.get_driver_scheduled_for_monthly),

    #     passengers notifications
    path('passengers_notifications/', views.get_all_passenger_notifications),
    path('get_passenger_notifications/', views.get_passenger_notifications),
    path('get_passengers_triggered_notifications/', views.get_passengers_triggered_notifications),

    #     notifications

    path('get_all_driver_notifications/', views.get_all_driver_notifications),
    path('user_notifications/', views.get_user_notifications),
    path('user_triggerd_notifications/', views.get_triggered_notifications),
    path('user_read_notifications/', views.read_notification),
    path("notification/<int:id>/", views.notification_detail),

    #     new wallet system
    path("admin_load_users_wallet/", views.admin_load_users_wallet),
    path("admin_get_all_users_wallet/", views.admin_get_all_users_wallet),
    path("user_wallet_detail/<int:id>/", views.user_wallet_detail),
    path("get_user_wallet_detail/<int:id>/", views.get_user_wallet_detail),
    path("admin_update_wallet/<int:id>/", views.admin_update_wallet),
    path("get_user_wallet/", views.get_user_wallet),
    path("user_update_wallet/<int:user>/", views.user_update_wallet),
    path("get_wallet_by_user/<int:user_id>/", views.get_wallet_by_user),
    path("get_wallet_by_username/<str:username>/", views.get_wallet_by_username),


    #     searches
    path("search_wallet/", views.SearchWallet.as_view()),
    path("search_ride_request/", views.SearchScheduleRequest.as_view()),

    # register and rent car
    path("register_car_for_rent/",views.register_car_for_rent),
    path("get_all_registered_vehicles/",views.get_all_registered_vehicles),
    path("update_vehicle/<int:id>/",views.update_vehicle),
    path("get_vehicle_detail/<int:id>/",views.get_vehicle_detail),
    path("rent_car/",views.rent_car),
    path("get_all_my_rented_car_details/",views.get_all_my_rented_car_details),
    path("update_my_rented_car_status/<int:id>/",views.update_my_rented_car_status),

    #
    path("add_image_to_registered_car/",views.add_image_to_registered_car),
    path("get_all_registered_images/<int:id>/",views.get_all_registered_images),
    ]

