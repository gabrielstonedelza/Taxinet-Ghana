# Generated by Django 4.0.3 on 2022-04-02 11:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taxinet_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sos',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='scheduleride',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='scheduleride',
            name='passenger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passenger_scheduling_ride', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='requestride',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='driver_to_accept_ride', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='requestride',
            name='passenger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ratedriver',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='driver_being_rated', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ratedriver',
            name='passenger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='notifications',
            name='notification_from',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='notifications',
            name='notification_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='User_receiving_notification', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='driverreviews',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='driverreviews',
            name='passenger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_giving_review', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='confirmdriverpayment',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
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
            model_name='acceptscheduleride',
            name='scheduled_ride',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Scheduled_Ride_to_accept', to='taxinet_api.scheduleride'),
        ),
        migrations.AddField(
            model_name='acceptscheduleride',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='acceptride',
            name='ride',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Ride_to_accept', to='taxinet_api.requestride'),
        ),
        migrations.AddField(
            model_name='acceptride',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
