# Generated by Django 4.0.3 on 2022-04-03 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxinet_api', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheduleride',
            name='confirmation_status',
        ),
    ]
