# Generated by Django 4.0.3 on 2022-08-30 20:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taxinet_users', '0002_alter_addtoverified_user'),
        ('taxinet_api', '0011_remove_driverendtrip_ride'),
    ]

    operations = [
        migrations.AddField(
            model_name='driverendtrip',
            name='ride',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='driverstarttrip',
            name='ride',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='drivervehicleinventory',
            name='millage',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='drivervehicleinventory',
            name='registration_number',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='drivervehicleinventory',
            name='unique_number',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='drivervehicleinventory',
            name='vehicle_brand',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.CreateModel(
            name='DriversWallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10)),
                ('date_loaded', models.DateTimeField(auto_now_add=True)),
                ('administrator', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='drivers_administrator_for_wallet', to=settings.AUTH_USER_MODEL)),
                ('driver', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='driver_only_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DriverAskToLoadWallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Wants to load wallet', max_length=200)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10)),
                ('date_requested', models.DateField(auto_now_add=True)),
                ('time_requested', models.TimeField(auto_now_add=True)),
                ('read', models.CharField(choices=[('Read', 'Read'), ('Not Read', 'Not Read')], default='Not Read', max_length=10)),
                ('administrator', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='administrator_loadWallet', to=settings.AUTH_USER_MODEL)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taxinet_users.passengerprofile')),
            ],
        ),
        migrations.CreateModel(
            name='DriverAddToUpdatedWallets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taxinet_api.driverswallet')),
            ],
        ),
    ]