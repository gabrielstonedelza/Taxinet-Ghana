# Generated by Django 4.0.3 on 2022-08-24 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxinet_api', '0004_alter_asktoloadwallet_date_requested_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedulednotifications',
            old_name='schedule_ride_id',
            new_name='schedule_ride_slug',
        ),
        migrations.RemoveField(
            model_name='schedulednotifications',
            name='message_id',
        ),
        migrations.AddField(
            model_name='schedulednotifications',
            name='schedule_ride_title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
