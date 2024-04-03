# Generated by Django 4.0.3 on 2024-04-03 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars_for_rent', '0001_initial'),
        ('pay_drive', '0010_addtoapprovedpayanddrive_dropped_off'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requestpayanddrive',
            name='payment_period',
        ),
        migrations.AddField(
            model_name='requestpayanddrive',
            name='referral',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='requestpayanddrive',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_for_pay_and_drive', to='cars_for_rent.carsforrent'),
        ),
    ]
