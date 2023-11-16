# Generated by Django 4.0.3 on 2023-11-16 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car_sales', '0003_vehicle_purpose'),
        ('pay_drive', '0003_requestpayanddrive_drive_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestpayanddrive',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_for_pay_and_drive', to='car_sales.vehicle'),
        ),
        migrations.AlterField(
            model_name='requestpayanddrive',
            name='request_approved',
            field=models.CharField(default='Pending', max_length=30),
        ),
    ]
