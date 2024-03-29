# Generated by Django 4.0.3 on 2023-11-14 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleRide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule_type', models.CharField(choices=[('School Pick up And Drop Off', 'School Pick up And Drop Off'), ('Office Pick up And Drop Off', 'Office Pick up And Drop Off'), ('Airport Pick up And Drop Off', 'Airport Pick up And Drop Off'), ('Delivery Pick up And Drop Off', 'Delivery Pick up And Drop Off'), ('Hotel Pick up And Drop Off', 'Hotel Pick up And Drop Off')], default='Airport Pick up And Drop Off', max_length=255)),
                ('schedule_duration', models.CharField(choices=[('One Time', 'One Time'), ('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Days', 'Days')], default='One Time', max_length=255)),
                ('pickup_location', models.CharField(blank=True, default='', max_length=255)),
                ('drop_off_location', models.CharField(blank=True, default='', max_length=255)),
                ('pick_up_time', models.CharField(blank=True, max_length=100)),
                ('start_date', models.CharField(blank=True, max_length=100)),
                ('completed', models.BooleanField(default=False)),
                ('days', models.CharField(blank=True, default='', max_length=15)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Active', 'Active'), ('Cancelled', 'Cancelled')], default='Pending', max_length=50)),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10)),
                ('charge', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10)),
                ('date_scheduled', models.DateField(auto_now_add=True)),
                ('time_scheduled', models.TimeField(auto_now_add=True)),
                ('pickup_lng', models.CharField(blank=True, default='', max_length=255)),
                ('pickup_lat', models.CharField(blank=True, default='', max_length=255)),
                ('drop_off_lat', models.CharField(blank=True, default='', max_length=255)),
                ('drop_off_lng', models.CharField(blank=True, default='', max_length=255)),
            ],
        ),
    ]
