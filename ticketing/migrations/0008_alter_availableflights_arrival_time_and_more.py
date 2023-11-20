# Generated by Django 4.0.3 on 2023-11-20 11:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0007_alter_requestbooking_adults_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availableflights',
            name='arrival_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='availableflights',
            name='departure_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='availableflights',
            name='departure_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='availableflights',
            name='returning_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='availableflights',
            name='returning_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
