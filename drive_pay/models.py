from django.db import models
from users.models import User

DRIVING_STYLE = (
    ("Self Drive","Self Drive"),
    ("With Driver","With Driver"),
)

class RequestDriveAndPay(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car  = models.CharField(max_length=100)
    drive_type = models.CharField(max_length=50,choices=DRIVING_STYLE,default="Self Drive")
    period = models.CharField(max_length=10)
    pick_up_date = models.CharField(max_length=10)
    drop_off_date = models.CharField(max_length=10)
    period_total_price = models.DecimalField(max_digits=19, decimal_places=2, default=0.0)
    request_approved = models.BooleanField(default=False)
    date_requested = models.DateTimeField(auto_now_add=True)

    def get_user_phone(self):
        return self.user.phone_number

    def __str__(self):
        return self.user.username


    def get_username(self):
        return self.user.username

class AddToApprovedDriveAndPay(models.Model):
    drive_and_pay = models.ForeignKey(RequestDriveAndPay,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="user_being_approved_for_dnp")
    assigned_driver = models.ForeignKey(User, on_delete=models.CASCADE,related_name="driver_being_approved_for_dnp",default=1)
    date_approved = models.DateTimeField(auto_now_add=True)




    def __str__(self):
        return self.user.username

    def get_car_name(self):
        return self.drive_and_pay.car

    def get_drive_type(self):
        return self.drive_and_pay.drive_type

    def get_pick_up_date(self):
        return self.drive_and_pay.pick_up_date
    def get_drop_off_date(self):
        return self.drive_and_pay.drop_off_date

    def get_payment_period(self):
        return self.drive_and_pay.period

    def get_total_price(self):
        return self.drive_and_pay.period_total_price


    def get_date_requested(self):
        return self.drive_and_pay.date_requested