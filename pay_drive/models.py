from django.db import models
from users.models import User
from car_sales.models import Vehicle


PAYMENT_PERIODS = (
    ("1 Yr","1 Yr"),
    ("2 Yrs","2 Yrs"),
    ("3 Yrs","3 Yrs"),
)

DRIVING_STYLE = (
    ("Self Drive","Self Drive"),
    ("With Driver","With Driver"),
)

class RequestPayAndDrive(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    car  = models.ForeignKey(Vehicle, on_delete=models.CASCADE,related_name="car_for_pay_and_drive")
    drive_type = models.CharField(max_length=50, choices=DRIVING_STYLE, default="Self Drive")
    pick_up_date = models.CharField(max_length=10)
    drop_off_date = models.CharField(max_length=10, default="")
    payment_period = models.CharField(max_length=10, choices=PAYMENT_PERIODS, default="1 Yr")
    period_total_price = models.DecimalField(max_digits=19, decimal_places=2, default=0.0)
    request_approved = models.CharField(max_length=30, default="Pending")
    date_requested = models.DateTimeField(auto_now_add=True)

    def get_user_phone(self):
        return self.user.phone_number

    def __str__(self):
        return self.user.username

    def get_username(self):
        return self.user.username

    def get_car_name(self):
        return self.car.name

    def get_car_pic(self):
        if self.car.picture:
            return "https://taxinetghana.xyz" + self.car.picture.url
        return ''


class AddToApprovedPayAndDrive(models.Model):
    pay_and_drive = models.ForeignKey(RequestPayAndDrive,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="user_being_approved")
    assigned_driver = models.ForeignKey(User, on_delete=models.CASCADE,related_name="driver_being_approved",default=1)
    date_approved = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def get_car_name(self):
        return self.pay_and_drive.car.name

    def get_driver_type(self):
        return self.pay_and_drive.drive_type

    def get_pick_up_date(self):
        return self.pay_and_drive.pick_up_date

    def get_payment_period(self):
        return self.pay_and_drive.payment_period

    def get_total_price(self):
        return self.pay_and_drive.period_total_price


    def get_date_requested(self):
        return self.pay_and_drive.date_requested


class PayDailyPayAndDrive(models.Model):
    approved_drive = models.ForeignKey(AddToApprovedPayAndDrive, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payment_daily")
    amount = models.DecimalField(max_digits=19, decimal_places=2, default=0.0)
    date_paid = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.username

class PayExtraDriveAndPay(models.Model):
    approved_drive = models.ForeignKey(AddToApprovedPayAndDrive, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payment_daily_pay_drive")
    amount = models.DecimalField(max_digits=19, decimal_places=2, default=0.0)
    date_paid = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username