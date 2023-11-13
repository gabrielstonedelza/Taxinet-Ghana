from django.db import models
from users.models import User


class RequestDriveAndPay(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car  = models.CharField(max_length=100)
    period = models.CharField(max_length=10)
    pick_up_date = models.CharField(max_length=10)
    drop_off_date = models.CharField(max_length=10)
    period_total_price = models.DecimalField(max_digits=19, decimal_places=2, default=0.0)
    request_approved = models.BooleanField(default=False)
    date_requested = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


    def get_username(self):
        return self.user.username
