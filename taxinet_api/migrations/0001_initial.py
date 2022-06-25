# Generated by Django 4.0.3 on 2022-06-25 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcceptedRides',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passengers_lat', models.CharField(max_length=255, null=True)),
                ('passengers_lng', models.CharField(max_length=255, null=True)),
                ('date_accepted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BidRide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10)),
                ('date_accepted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BidScheduleRide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid', models.CharField(blank=True, max_length=10)),
                ('date_accepted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Complains',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complain', models.TextField(blank=True)),
                ('read', models.BooleanField(default=False)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CompletedBidOnRide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drivers_lat', models.CharField(blank=True, max_length=255, null=True)),
                ('drivers_lng', models.CharField(blank=True, max_length=255, null=True)),
                ('passengers_pickup', models.CharField(blank=True, max_length=255, null=True)),
                ('pick_up_place_id', models.CharField(blank=True, max_length=255, null=True)),
                ('date_accepted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CompletedRides',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_completed', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ConfirmDriverPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_confirmed', models.BooleanField(default=False)),
                ('bank_payment_reference', models.CharField(max_length=100)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10)),
                ('date_confirmed', models.DateTimeField(auto_now_add=True)),
                ('date_posted', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DriverReviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviews', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='DriversLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_id', models.CharField(blank=True, max_length=100)),
                ('location_name', models.CharField(default='', max_length=100)),
                ('drivers_lat', models.CharField(blank=True, max_length=255, null=True)),
                ('drivers_lng', models.CharField(blank=True, max_length=255, null=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='DriversPoints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(default=0)),
                ('date_rated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_id', models.CharField(blank=True, default='', max_length=100)),
                ('notification_tag', models.CharField(blank=True, default='', max_length=255)),
                ('notification_title', models.CharField(blank=True, max_length=255)),
                ('notification_message', models.TextField(blank=True)),
                ('read', models.CharField(choices=[('Read', 'Read'), ('Not Read', 'Not Read')], default='Not Read', max_length=20)),
                ('notification_trigger', models.CharField(blank=True, choices=[('Triggered', 'Triggered'), ('Not Triggered', 'Not Triggered')], default='Triggered', max_length=255)),
                ('drop_off_lat', models.CharField(max_length=255, null=True)),
                ('drop_off_lng', models.CharField(max_length=255, null=True)),
                ('passengers_lat', models.CharField(blank=True, max_length=255, null=True)),
                ('passengers_lng', models.CharField(blank=True, max_length=255, null=True)),
                ('drivers_lat', models.CharField(blank=True, max_length=255, null=True)),
                ('drivers_lng', models.CharField(blank=True, max_length=255, null=True)),
                ('passengers_pickup', models.CharField(blank=True, max_length=255, null=True)),
                ('passengers_dropOff', models.CharField(blank=True, max_length=255, null=True)),
                ('ride_id', models.CharField(blank=True, max_length=100)),
                ('ride_accepted_id', models.CharField(blank=True, max_length=255)),
                ('ride_rejected_id', models.CharField(blank=True, max_length=255)),
                ('completed_ride_id', models.CharField(blank=True, max_length=255)),
                ('schedule_ride_id', models.CharField(blank=True, max_length=255)),
                ('schedule_accepted_id', models.CharField(blank=True, max_length=255)),
                ('pick_up_place_id', models.CharField(blank=True, default='', max_length=255)),
                ('drop_off_place_id', models.CharField(blank=True, default='', max_length=255)),
                ('message_id', models.CharField(blank=True, default='', max_length=255)),
                ('schedule_rejected_id', models.CharField(blank=True, max_length=255)),
                ('complain_id', models.CharField(blank=True, max_length=255)),
                ('reply_id', models.CharField(blank=True, max_length=255)),
                ('review_id', models.CharField(blank=True, max_length=255)),
                ('rating_id', models.CharField(blank=True, max_length=255)),
                ('payment_confirmed_id', models.CharField(blank=True, max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='RejectedRides',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_rejected', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='RequestRide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pick_up', models.CharField(blank=True, max_length=255)),
                ('drop_off', models.CharField(blank=True, max_length=255)),
                ('ride_accepted', models.BooleanField(default=False)),
                ('ride_rejected', models.BooleanField(default=False)),
                ('passengers_lat', models.CharField(max_length=255, null=True)),
                ('passengers_lng', models.CharField(max_length=255, null=True)),
                ('drop_off_lat', models.CharField(max_length=255, null=True)),
                ('drop_off_lng', models.CharField(max_length=255, null=True)),
                ('passengers_pick_up_place_id', models.CharField(blank=True, default='', max_length=255)),
                ('passengers_drop_off_place_id', models.CharField(blank=True, default='', max_length=255)),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10)),
                ('completed', models.BooleanField(default=False)),
                ('bid_completed', models.BooleanField(default=False)),
                ('driver_booked', models.BooleanField(default=False)),
                ('driver_on_route', models.BooleanField(default=False)),
                ('passenger_boarded', models.BooleanField(default=False)),
                ('date_requested', models.DateField(auto_now_add=True)),
                ('time_requested', models.TimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleRide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_pickup', models.DateField(blank=True)),
                ('time_of_pickup', models.TimeField(blank=True)),
                ('schedule_option', models.CharField(choices=[('One Time', 'One Time'), ('Daily', 'Daily'), ('Days', 'Days'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly')], default='One Time', max_length=30)),
                ('pickup_location', models.CharField(blank=True, max_length=255)),
                ('drop_off_location', models.CharField(blank=True, max_length=255)),
                ('scheduled', models.BooleanField(default=False)),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10)),
                ('initial_payment', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10)),
                ('date_scheduled', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SearchedDestinations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('searched_destination', models.CharField(max_length=255)),
                ('place_id', models.CharField(default='', max_length=255)),
                ('drop_off_lat', models.CharField(max_length=255, null=True)),
                ('drop_off_lng', models.CharField(max_length=255, null=True)),
                ('date_searched', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(blank=True, max_length=255)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
