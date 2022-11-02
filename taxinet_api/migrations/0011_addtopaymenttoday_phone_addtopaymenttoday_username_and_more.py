# Generated by Django 4.0.3 on 2022-10-31 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxinet_api', '0010_alter_wallets_phone_alter_wallets_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='addtopaymenttoday',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='addtopaymenttoday',
            name='username',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='scheduleride',
            name='driver_phone',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='scheduleride',
            name='driver_username',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='scheduleride',
            name='passenger_phone',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='scheduleride',
            name='passenger_username',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]