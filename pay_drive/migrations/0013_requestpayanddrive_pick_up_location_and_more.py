# Generated by Django 4.0.3 on 2024-04-13 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay_drive', '0012_alter_requestpayanddrive_referral'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestpayanddrive',
            name='pick_up_location',
            field=models.CharField(blank=True, default='', max_length=120),
        ),
        migrations.AddField(
            model_name='requestpayanddrive',
            name='pick_up_time',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
    ]