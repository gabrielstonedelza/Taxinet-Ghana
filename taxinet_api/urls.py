from django.urls import path

from . import views

urlpatterns = [

    # vehicles
    path("vehicle_detail/<int:id>/", views.get_vehicle_detail),
    path("vehicle_update/<int:id>/", views.update_vehicle),
    path("all_vehicles/", views.get_all_registered_vehicles),

    path("admin_get_all_requests/", views.admin_get_all_requests),
    path("admin_request_detail/<str:id>/", views.admin_ride_detail),
    path("admin_update_requested_ride/<int:id>/", views.admin_update_requested_ride),

    path("admin_get_cancelled_schedules/", views.admin_get_cancelled_schedules),

    path('get_all_my_ride_requests/', views.get_all_my_ride_requests),
    path('ride_requests/<int:id>/', views.ride_detail),
    path('request_ride/new/', views.request_ride),
    path('update_requested_ride/<int:ride_id>/', views.update_requested_ride),
    path('delete_requested_ride/<int:ride_id>/', views.delete_requested_ride),

    #     Complains
    path('complains/new/', views.post_complain),
    path('all_complains/', views.get_all_complains),
    path('user_complains/', views.user_complains),
    path('complain/<int:complain_id>/', views.get_detailed_complain),

    #     drivers confirmed payment
    path('cancel_schedule/', views.cancel_schedule),

    path("post_to_contact/", views.send_to_contact),
    path("get_all_contact_us_messages/", views.get_all_contact_us_messages),

    #     notifications
    path('user_notifications/', views.get_user_notifications),
    path('user_triggerd_notifications/', views.get_triggered_notifications),
    path('user_read_notifications/', views.read_notification),
    path("notification/<int:id>/", views.notification_detail),

    #     new wallet system
    path("admin_load_users_wallet/", views.admin_load_users_wallet),
    path("admin_get_all_users_wallet/", views.admin_get_all_users_wallet),
    path("get_user_wallet_detail/<int:id>/", views.get_user_wallet_detail),
    path("admin_update_wallet/<int:id>/", views.admin_update_wallet),
    path("get_user_wallet/", views.get_user_wallet),


    #     searches
    path("search_wallet/", views.SearchWallet.as_view()),
    path("search_ride_request/", views.SearchScheduleRequest.as_view()),

    # register and rent car
    path("register_car_for_rent/",views.register_car_for_rent),
    path("get_all_registered_vehicles/",views.get_all_registered_vehicles),
    path("update_vehicle/<int:id>/",views.update_vehicle),
    path("get_vehicle_detail/<int:id>/",views.get_vehicle_detail),
    path("delete_vehicle/<int:pk>/",views.delete_vehicle),
    path("rent_car/",views.rent_car),
    path("get_all_my_rented_car_details/",views.get_all_my_rented_car_details),
    path("update_my_rented_car_status/<int:id>/",views.update_my_rented_car_status),
    path("delete_my_rented_request/<int:pk>/",views.delete_my_rented_request),

    #
    path("add_image_to_registered_car/",views.add_image_to_registered_car),
    path("get_all_registered_images/<int:id>/",views.get_all_registered_images),
    ]

