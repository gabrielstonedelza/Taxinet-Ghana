# Generated by Django 4.0.3 on 2024-05-09 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_for_rent', '0004_carsforrent_car_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='carsforrent',
            name='transmission',
            field=models.CharField(default='Automatic', max_length=100),
        ),
    ]