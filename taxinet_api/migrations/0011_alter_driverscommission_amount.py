# Generated by Django 4.0.3 on 2022-11-16 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxinet_api', '0010_walletdeduction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driverscommission',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=19),
        ),
    ]