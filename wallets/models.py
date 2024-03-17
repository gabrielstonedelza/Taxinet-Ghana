from django.db import models
from users.models import User

class Wallets(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_with_wallet")
    amount = models.DecimalField(decimal_places=2, max_digits=10, default=00.00)
    date_loaded = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.pk)

    def get_user_phone(self):
        return self.user.phone_number

    def get_username(self):
        return self.user.username

    def get_full_name(self):
        return self.user.full_name


class UpdatedWallets(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_with_updated_wallet")
    wallet = models.ForeignKey(Wallets, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=10, default=00.00)
    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.wallet.user.username}'s wallet was updated."

    def get_username(self):
        return self.user.username

    def get_full_name(self):
        return self.user.full_name