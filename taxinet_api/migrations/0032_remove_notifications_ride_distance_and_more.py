# Generated by Django 4.0.3 on 2022-06-14 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxinet_api', '0031_notifications_message_id_requestride_driver_on_route_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notifications',
            name='ride_distance',
        ),
        migrations.RemoveField(
            model_name='notifications',
            name='ride_duration',
        ),
        migrations.RemoveField(
            model_name='requestride',
            name='ride_distance',
        ),
        migrations.RemoveField(
            model_name='requestride',
            name='ride_duration',
        ),
    ]