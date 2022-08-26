# Generated by Django 4.0.3 on 2022-08-26 13:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taxinet_api', '0005_schedulednotifications_schedule_ride_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asktoloadwallet',
            name='passenger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
