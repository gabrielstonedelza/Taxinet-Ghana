# Generated by Django 4.0.3 on 2022-10-31 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxinet_api', '0009_wallets_phone_wallets_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallets',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='wallets',
            name='username',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
