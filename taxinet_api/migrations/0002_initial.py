# Generated by Django 4.0.3 on 2022-08-25 22:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taxinet_api', '0001_initial'),
        ('taxinet_users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduleride',
            name='administrator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='scheduleride',
            name='assigned_driver',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='driver_to_be_assigned_schedule', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='scheduleride',
            name='passenger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passenger_scheduling_ride', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='schedulednotifications',
            name='notification_from',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='schedulednotifications',
            name='notification_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='DeUser_receiving_notification', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='schedulednotifications',
            name='notification_to_passenger',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Passenger_receiving_notification', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rejectedscheduledrides',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='driver_rejecting_scheduled_ride', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rejectedscheduledrides',
            name='scheduled_ride',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taxinet_api.scheduleride'),
        ),
        migrations.AddField(
            model_name='rejectassignedscheduled',
            name='assigned_to_driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taxinet_api.assignscheduletodriver'),
        ),
        migrations.AddField(
            model_name='rejectassignedscheduled',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='passengerswallet',
            name='administrator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='administrator_for_wallet', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='passengerswallet',
            name='passenger',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='passenger_only_profile', to='taxinet_users.passengerprofile'),
        ),
        migrations.AddField(
            model_name='drivervehicleinventory',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='driverslocation',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contactadmin',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='confirmdriverpayment',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='completedscheduledridestoday',
            name='scheduled_ride',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taxinet_api.scheduleride'),
        ),
        migrations.AddField(
            model_name='complains',
            name='complainant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_making_complain', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='complains',
            name='offender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cancelscheduledride',
            name='passenger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passenger_cancelling_ride', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cancelscheduledride',
            name='ride',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taxinet_api.scheduleride'),
        ),
        migrations.AddField(
            model_name='assignscheduletodriver',
            name='administrator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='assignscheduletodriver',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Driver_receiving_scheduled_ride', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='assignscheduletodriver',
            name='ride',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taxinet_api.scheduleride'),
        ),
        migrations.AddField(
            model_name='asktoloadwallet',
            name='administrator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='administrator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='asktoloadwallet',
            name='passenger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taxinet_users.passengerprofile'),
        ),
        migrations.AddField(
            model_name='addtoupdatedwallets',
            name='wallet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taxinet_api.passengerswallet'),
        ),
        migrations.AddField(
            model_name='acceptedscheduledrides',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='driver_accepting_scheduled_ride', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='acceptedscheduledrides',
            name='scheduled_ride',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taxinet_api.scheduleride'),
        ),
        migrations.AddField(
            model_name='acceptassignedscheduled',
            name='assigned_to_driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taxinet_api.assignscheduletodriver'),
        ),
        migrations.AddField(
            model_name='acceptassignedscheduled',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
