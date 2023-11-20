# Generated by Django 4.0.3 on 2023-11-20 12:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0008_alter_availableflights_arrival_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='availableflights',
            name='arrival_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='availableflights',
            name='arrival_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='availableflights',
            name='departure_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='availableflights',
            name='departure_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='availableflights',
            name='returning_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='availableflights',
            name='returning_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
