# Generated by Django 4.0.3 on 2023-11-20 13:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0009_availableflights_arrival_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='availableflights',
            name='flight_type',
        ),
        migrations.RemoveField(
            model_name='availableflights',
            name='returning_date',
        ),
        migrations.RemoveField(
            model_name='availableflights',
            name='returning_time',
        ),
        migrations.AddField(
            model_name='booking',
            name='flight_type',
            field=models.CharField(choices=[('Round Trip', 'Round Trip'), ('One Way', 'One Way')], default='Round Trip', max_length=100),
        ),
        migrations.AddField(
            model_name='booking',
            name='returning_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='booking',
            name='returning_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='availableflights',
            name='arrival_airport',
            field=models.CharField(choices=[('Kumasi (KMS)', 'Kumasi (KMS)'), ('Accra (ACC)', 'Accra (ACC)'), ('Takoradi (TKD)', 'Takoradi (TKD)'), ('Tamale (TML)', 'Tamale (TML)'), ('Wa (WZA)', 'Wa (AWZA'), ('Sunyani (NYI)', 'Sunyani (NYI)')], default='Kumasi (KSI)', max_length=100),
        ),
        migrations.AlterField(
            model_name='availableflights',
            name='departure_airport',
            field=models.CharField(choices=[('Kumasi (KMS)', 'Kumasi (KMS)'), ('Accra (ACC)', 'Accra (ACC)'), ('Takoradi (TKD)', 'Takoradi (TKD)'), ('Tamale (TML)', 'Tamale (TML)'), ('Wa (WZA)', 'Wa (AWZA'), ('Sunyani (NYI)', 'Sunyani (NYI)')], default='Kumasi (KSI)', max_length=100),
        ),
        migrations.AlterField(
            model_name='booking',
            name='infants',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='0', max_length=11),
        ),
    ]
