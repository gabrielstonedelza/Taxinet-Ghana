# Generated by Django 4.0.3 on 2024-05-27 21:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pay_drive', '0014_addtoapprovedpayanddrive_time_approved_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestpayanddrive',
            name='time_requested',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='requestpayanddrive',
            name='date_requested',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
