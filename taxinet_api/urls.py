from django.urls import path

from . import views

urlpatterns = [
    # admin urls
    path("admin_add_driver_to_work_and_pay/", views.admin_add_driver_to_work_and_pay),
    path("admin_get_all_work_and_pay/", views.admin_get_all_work_and_pay),
    path("work_and_pay_detail/<int:id>/", views.work_and_pay_detail),
    path("get_all_payments_today/", views.get_all_payments_today),
    path("admin_get_payment_detail/<int:id>/", views.admin_get_payment_detail),
    path("admin_get_all_drivers_payments_by_date/<str:payment_date>/",
         views.admin_get_all_drivers_payments_by_date),
    path("vehicle_detail/<int:id>/", views.vehicle_detail),
    path("vehicle_update/<int:id>/", views.update_vehicle),
    path("all_vehicles/", views.admin_get_all_registered_vehicles),
    path("admin_register_vehicle/", views.admin_register_vehicle),
    path("delete_assigned_driver/<int:pk>/", views.delete_assigned_driver),
    path("admin_load_passengers_wallet/", views.admin_load_passengers_wallet),
    path("admin_get_all_passengers_wallet/", views.admin_get_all_passengers_wallet),
    path("wallet_detail/<int:id>/", views.wallet_detail),
    path("update_wallet/<int:id>/", views.update_wallet),
    path("load_wallet_detail/<int:id>/", views.load_wallet_detail),
    path("admin_get_all_request_to_load_wallet/", views.admin_get_all_request_to_load_wallet),
    path("admin_get_all_requests/", views.admin_get_all_requests),
    path("admin_get_all_requests_by_date/<str:request_date>/", views.admin_get_all_requests_by_date),
    path("admin_get_five_requests/", views.admin_get_five_requests),
    path("admin_request_detail/<str:slug>/", views.admin_ride_detail),
    path("admin_update_requested_ride/<str:slug>/", views.admin_update_requested_ride),
    path("admin_assign_request_to_driver/", views.admin_assign_request_to_driver),
    path("admin_get_all_assigned_drivers/", views.admin_get_all_assigned_drivers),
    path("add_to_updated_wallets/", views.add_to_updated_wallets),

    path("admin_get_all_drivers_inventories/", views.admin_get_all_drivers_inventories),
    path("admin_get_all_drivers_inventories_by_date/<str:inventory_date>/",
         views.admin_get_all_drivers_inventories_by_date),
    path("admin_get_inventories_today/", views.admin_get_inventories_today),
    path("admin_get_driver_inventory/<int:driver_id>/", views.admin_get_driver_inventory),
    path("admin_get_driver_inventory_detail/<int:id>/", views.admin_get_inventory_detail),
    path("admin_get_pending_schedules/", views.admin_get_pending_schedules),
    path("admin_get_reviewing_schedules/", views.admin_get_reviewing_schedules),
    path("admin_get_active_schedules/", views.admin_get_active_schedules),
    path("admin_get_cancelled_schedules/", views.admin_get_cancelled_schedules),
    path("admin_get_scheduled_for_weekly/", views.admin_get_scheduled_for_weekly),
    path("admin_get_scheduled_for_days/", views.admin_get_scheduled_for_days),
    path("admin_get_scheduled_for_daily/", views.admin_get_scheduled_for_daily),
    path("admin_get_scheduled_for_one_time/", views.admin_get_scheduled_for_one_time),
    path("admin_get_all_user_notifications/", views.admin_get_all_user_notifications),
    # admin urls
    path('all_ride_requests/', views.get_all_requests),
    path('get_all_my_ride_requests/', views.get_all_my_ride_requests),
    path('ride_requests/<str:slug>/', views.ride_detail),
    path('passengers_requests_completed/', views.get_passengers_requests_completed),
    path('drivers_requests_completed/', views.get_drivers_requests_completed),
    path('passengers_requests_uncompleted/', views.get_passengers_requests_uncompleted),
    path('drivers_requests_uncompleted/', views.get_drivers_requests_uncompleted),
    path('request_ride/new/', views.request_ride),
    path('update_requested_ride/<int:ride_id>/', views.update_requested_ride),
    path('delete_requested_ride/<int:ride_id>/', views.delete_requested_ride),
    path('get_all_rejected_rides/', views.get_all_rejected_rides),
    path('add_to_rejected_rides/', views.add_to_rejected_rides),
    path('get_all_accepted_rides/', views.get_all_accepted_rides),
    path('add_to_accepted_rides/', views.add_to_accepted_rides),

    path('get_all_completed_rides/', views.get_all_completed_rides),
    path('add_to_completed_rides/', views.add_to_completed_rides),

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

    #     drivers confirmed payments
    path('payment/new/', views.post_payment),
    path('get_drivers_payments/', views.get_all_driver_payments),

    #     drivers inventoryOptions
    path("get_driver_inventory/", views.get_driver_inventory),
    path("get_all_drivers_inventories/", views.get_all_drivers_inventories),
    path("add_drivers_inventories/", views.create_drivers_inventory),
    path("driver_inventory_details/<int:id>/", views.drivers_inventory_detail),

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

    #     wallets
    path("request_to_load_wallet/", views.request_to_load_wallet),
    path("get_my_wallet/", views.get_my_wallet),

    #     passengers schedules
    path("get_my_active_schedules/", views.get_my_active_schedules),

    #     driver start and end trips
    path('driver_start_trip/', views.driver_start_trip),
    path('driver_end_trip/', views.driver_end_trip),

    #     driver alert arrrival
    path("driver_alert_passenger/", views.driver_alert_passenger),
    #
    path("get_drives_assigned_schedules/", views.get_drives_assigned_schedules),
    path("get_drives_assigned_and_active_schedules/", views.get_drives_assigned_and_active_schedules),

    #     driver get schedule types
    path('get_driver_scheduled_for_one_time/', views.get_driver_scheduled_for_one_time),
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
    path('user_read_notifications/<int:id>/', views.read_notification),
    path("notification/<int:id>/", views.notification_detail),

    #     drivers wallet
    path('add_to_drivers_updated_wallets/', views.add_to_drivers_updated_wallets),
    path('admin_load_drivers_wallet/', views.admin_load_drivers_wallet),
    path('admin_get_all_drivers_wallet/', views.admin_get_all_drivers_wallet),
    path('get_drivers_wallet/', views.get_drivers_wallet),
    path('request_to_load_drivers_wallet/', views.request_to_load_drivers_wallet),
    path('admin_get_all_drivers_request_to_load_wallet/', views.admin_get_all_drivers_request_to_load_wallet),
    path('drivers_wallet_detail/<int:id>/', views.drivers_wallet_detail),
    path('update_drivers_wallet/<int:id>/', views.update_drivers_wallet),
    path('load_drivers_wallet_detail/<int:id>/', views.load_drivers_wallet_detail),

    #     drivers payments_today
    path("add_to_drivers_payment_today/", views.add_to_drivers_payment_today),

    #     drivers work and pay
    path("get_my_work_and_pay/", views.get_my_work_and_pay),
    path("get_work_and_pay_detail/<int:id>/", views.get_work_and_pay_detail),

    #     drivers daily payments
    path("payment_today/", views.payments_today),
    path("payment_detail<int:id>/", views.payment_detail),

    #     other wallet transfers
    path("transfer_to_wallet/", views.transfer_to_wallet),

    #     new wallet system
    path("admin_load_users_wallet/", views.admin_load_users_wallet),
    path("admin_get_all_users_wallet/", views.admin_get_all_users_wallet),
    path("user_wallet_detail/<int:id>/", views.user_wallet_detail),
    path("admin_update_wallet/<int:id>/", views.admin_update_wallet),
    path("admin_get_load_wallet_requests_detail/<int:id>/", views.admin_get_load_wallet_requests_detail),
    path("get_all_request_to_load_wallet/", views.get_all_request_to_load_wallet),
    path("admin_add_to_updated_wallets/", views.admin_add_to_updated_wallets),
    path("user_request_to_load_wallet/", views.user_request_to_load_wallet),
    path("get_user_wallet/", views.get_user_wallet),
    path("user_update_wallet/<int:user>/", views.user_update_wallet),
    path("get_wallet_by_user/<int:user_id>/", views.get_wallet_by_user),

    #     driver and passenger messages on ride
    path("send_message/<str:slug>/", views.send_message),
    path("get_all_ride_messages/<int:id>/", views.get_all_ride_messages),

]
