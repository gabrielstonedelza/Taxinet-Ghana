from django.db import models

class Referrals(models.Model):
    name = models.CharField(max_length=150,unique=True)
    phone = models.CharField(max_length=20,unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ReferralWallets(models.Model):
    referral = models.ForeignKey(Referrals, on_delete=models.CASCADE, related_name="referral_with_wallet")
    amount = models.DecimalField(decimal_places=2, max_digits=10, default=00.00)
    date_loaded = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.pk)

    def get_referral_phone(self):
        return self.referral.phone

    def get_referral_name(self):
        return self.referral.name

class UpdatedReferralWallets(models.Model):
    referral = models.ForeignKey(Referrals, on_delete=models.CASCADE, related_name="referral_with_updated_wallet")
    referral_wallet = models.ForeignKey(ReferralWallets, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=10, default=00.00)
    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.referral.name}'s wallet was updated."

    def get_name(self):
        return self.referral.name

