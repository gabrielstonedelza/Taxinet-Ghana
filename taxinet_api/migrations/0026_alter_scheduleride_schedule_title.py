# Generated by Django 4.0.3 on 2022-09-08 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxinet_api', '0025_alter_driverendtrip_payment_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduleride',
            name='schedule_title',
            field=models.CharField(default='', max_length=255, unique=True),
        ),
    ]
