# Generated by Django 4.0.3 on 2022-10-31 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxinet_users', '0002_alter_user_user_type_rideadminprofile_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='driverprofile',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='driverprofile',
            name='username',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='investorsprofile',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='investorsprofile',
            name='username',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='passengerprofile',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='passengerprofile',
            name='username',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
