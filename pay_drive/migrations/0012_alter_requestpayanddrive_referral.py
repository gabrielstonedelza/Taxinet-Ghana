# Generated by Django 4.0.3 on 2024-04-03 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay_drive', '0011_remove_requestpayanddrive_payment_period_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestpayanddrive',
            name='referral',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
    ]
