# Generated by Django 4.0.3 on 2022-11-16 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxinet_api', '0011_alter_driverscommission_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drivertransfercommissiontowallet',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=19),
        ),
    ]