# Generated by Django 4.0.3 on 2024-04-01 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay_drive', '0007_payextradriveandpay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestpayanddrive',
            name='request_approved',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending', max_length=30),
        ),
    ]
