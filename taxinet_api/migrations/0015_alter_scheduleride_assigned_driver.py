# Generated by Django 4.0.3 on 2022-08-11 16:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taxinet_api', '0014_scheduleride_assigned_driver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduleride',
            name='assigned_driver',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='driver_to_be_assigned_schedule', to=settings.AUTH_USER_MODEL),
        ),
    ]