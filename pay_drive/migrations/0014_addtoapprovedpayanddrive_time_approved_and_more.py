# Generated by Django 4.0.3 on 2024-05-27 19:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pay_drive', '0013_requestpayanddrive_pick_up_location_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='addtoapprovedpayanddrive',
            name='time_approved',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='addtoapprovedpayanddrive',
            name='date_approved',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='requestpayanddrive',
            name='drive_type',
            field=models.CharField(choices=[('Self Drive', 'Self Drive'), ('With a Driver', 'With a Driver')], default='Self Drive', max_length=50),
        ),
    ]