# Generated by Django 4.0.3 on 2022-08-11 11:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taxinet_api', '0013_remove_scheduleride_assigned_driver'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduleride',
            name='assigned_driver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='driver_to_be_assigned_schedule', to=settings.AUTH_USER_MODEL),
        ),
    ]
