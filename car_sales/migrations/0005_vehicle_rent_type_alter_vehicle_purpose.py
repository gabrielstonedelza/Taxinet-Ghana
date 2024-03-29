# Generated by Django 4.0.3 on 2023-11-18 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_sales', '0004_buyvehicle_request_approved_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='rent_type',
            field=models.CharField(choices=[('Pay And Drive', 'Pay And Drive'), ('Drive And Pay', 'Drive And Pay')], default='Pay And Drive', max_length=50),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='purpose',
            field=models.CharField(choices=[('For Sale', 'For Sale'), ('For Rent', 'For Rent')], default='For Sale', max_length=50),
        ),
    ]
