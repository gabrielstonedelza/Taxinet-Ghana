# Generated by Django 4.0.3 on 2022-11-16 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxinet_users', '0006_accountsprofile_unique_code_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountsprofile',
            name='unique_code',
        ),
        migrations.RemoveField(
            model_name='driverprofile',
            name='unique_code',
        ),
        migrations.RemoveField(
            model_name='passengerprofile',
            name='unique_code',
        ),
        migrations.RemoveField(
            model_name='promoterprofile',
            name='unique_code',
        ),
        migrations.AddField(
            model_name='user',
            name='unique_code',
            field=models.CharField(default='', max_length=500),
        ),
    ]
