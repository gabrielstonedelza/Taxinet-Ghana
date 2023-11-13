from django.db import models
from users.models import User


PAYMENT_PERIODS = (
    ("1 Yr","1 Yr"),
    ("2 Yrs","2 Yrs"),
    ("3 Yrs","3 Yrs"),
)

class RequestPayAndDrive(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    car = models.CharField(max_length=100)
    pick_up_date = models.CharField(max_length=10)
    payment_period = models.CharField(max_length=10, choices=PAYMENT_PERIODS, default="1 Yr")
    period_total_price = models.DecimalField(max_digits=19, decimal_places=2, default=0.0)
    request_approved = models.BooleanField(default=False)
    date_requested = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def get_username(self):
        return self.user.username