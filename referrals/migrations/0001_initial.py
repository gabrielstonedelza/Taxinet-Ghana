# Generated by Django 4.0.3 on 2024-04-03 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Referrals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('phone', models.CharField(max_length=20, unique=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReferralWallets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('date_loaded', models.DateTimeField(auto_now_add=True)),
                ('referral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='referral_with_wallet', to='referrals.referrals')),
            ],
        ),
        migrations.CreateModel(
            name='UpdatedReferralWallets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('referral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='referral_with_updated_wallet', to='referrals.referrals')),
                ('referral_wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='referrals.referralwallets')),
            ],
        ),
    ]