from django.contrib import admin

from .models import (ScheduleRide, Complains, ConfirmDriverPayment, AcceptedScheduledRides,
                     RejectedScheduledRides, DriverVehicleInventory,
                     CompletedScheduledRides, ScheduledNotifications, AssignScheduleToDriver,
                     AcceptAssignedScheduled,
                     RejectAssignedScheduled, CancelScheduledRide, ContactUs, ContactAdmin, PassengersWallet,
                     AskToLoadWallet, AddToUpdatedWallets, DriverStartTrip, DriverEndTrip, DriverAlertArrival,
                     DriversWallet, DriverAddToUpdatedWallets, DriverAskToLoadWallet, RegisterVehicle,
                     AddToPaymentToday, WorkAndPay, OtherWallet, Wallets, LoadWallet, UpdatedWallets, RideMessages,
                     ExpensesRequest,PrivateUserMessage, Stocks, MonthlySalary,
                     PayPromoterCommission, PrivateChatId, AddToBlockList, DriversCommission, WalletAddition,DriverRequestCommission, DriverTransferCommissionToWallet,WalletDeduction, WorkExtra, CallForInspection, UserRequestTopUp)


class AdminScheduleRide(admin.ModelAdmin):
    list_display = ['id', 'assigned_driver', 'passenger', 'schedule_type',
                    'ride_type', 'pickup_location', 'drop_off_location', 'pick_up_time',
                    'start_date', 'status', 'price', 'charge', 'date_scheduled']
    search_fields = ['id', 'passenger', 'assigned_driver']

    class Meta:
        model = ScheduleRide


admin.site.register(WalletAddition)
admin.site.register(UserRequestTopUp)
admin.site.register(CallForInspection)
admin.site.register(WorkExtra)
admin.site.register(DriversCommission)
admin.site.register(WalletDeduction)
admin.site.register(DriverTransferCommissionToWallet)
admin.site.register(DriverRequestCommission)
admin.site.register(PrivateUserMessage)
admin.site.register(Stocks)
admin.site.register(MonthlySalary)
admin.site.register(PayPromoterCommission)
admin.site.register(PrivateChatId)
admin.site.register(AddToBlockList)
admin.site.register(ExpensesRequest)
admin.site.register(RideMessages)
admin.site.register(LoadWallet)
admin.site.register(UpdatedWallets)
admin.site.register(DriverVehicleInventory)
admin.site.register(DriversWallet)
admin.site.register(DriverAddToUpdatedWallets)
admin.site.register(DriverAskToLoadWallet)
admin.site.register(ScheduleRide, AdminScheduleRide)
admin.site.register(AssignScheduleToDriver)
admin.site.register(AcceptAssignedScheduled)
admin.site.register(RejectAssignedScheduled)
admin.site.register(CancelScheduledRide)
admin.site.register(AcceptedScheduledRides)
admin.site.register(Complains)
admin.site.register(RejectedScheduledRides)
admin.site.register(CompletedScheduledRides)
admin.site.register(ConfirmDriverPayment)
admin.site.register(ScheduledNotifications)
admin.site.register(ContactUs)
admin.site.register(ContactAdmin)
admin.site.register(PassengersWallet)
admin.site.register(AskToLoadWallet)
admin.site.register(AddToUpdatedWallets)
admin.site.register(DriverStartTrip)
admin.site.register(DriverEndTrip)
admin.site.register(DriverAlertArrival)
admin.site.register(RegisterVehicle)
admin.site.register(AddToPaymentToday)
admin.site.register(WorkAndPay)
admin.site.register(OtherWallet)
admin.site.register(Wallets)
