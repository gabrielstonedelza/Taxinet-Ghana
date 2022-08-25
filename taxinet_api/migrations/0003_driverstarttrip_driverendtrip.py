# Generated by Django 4.0.3 on 2022-08-25 23:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taxinet_api', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DriverStartTrip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_started', models.DateField(auto_now_add=True)),
                ('time_started', models.TimeField(auto_now_add=True)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passenger_enjoying_trip', to=settings.AUTH_USER_MODEL)),
                ('ride', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trip_ride', to='taxinet_api.scheduleride')),
            ],
        ),
        migrations.CreateModel(
            name='DriverEndTrip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10)),
                ('date_stopped', models.DateField(auto_now_add=True)),
                ('time_stopped', models.TimeField(auto_now_add=True)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passenger_enjoying_trip_to_end', to=settings.AUTH_USER_MODEL)),
                ('ride', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trip_ride_end', to='taxinet_api.scheduleride')),
            ],
        ),
    ]