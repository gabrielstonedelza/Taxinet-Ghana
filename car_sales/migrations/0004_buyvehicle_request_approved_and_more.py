# Generated by Django 4.0.3 on 2023-11-17 08:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('car_sales', '0003_vehicle_purpose'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyvehicle',
            name='request_approved',
            field=models.CharField(default='Pending', max_length=50),
        ),
        migrations.CreateModel(
            name='AddToApprovedVehiclePurchases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_approved', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_sales.vehicle')),
            ],
        ),
    ]