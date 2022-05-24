# Generated by Django 4.0.3 on 2022-05-24 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxinet_api', '0016_notifications_passengers_dropff_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='ride_distance',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='notifications',
            name='ride_duration',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='requestride',
            name='ride_distance',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='requestride',
            name='ride_duration',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
