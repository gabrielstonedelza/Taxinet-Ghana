# Generated by Django 4.0.3 on 2022-07-10 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxinet_api', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduleride',
            name='ride_type',
            field=models.CharField(default='', max_length=30),
        ),
    ]
