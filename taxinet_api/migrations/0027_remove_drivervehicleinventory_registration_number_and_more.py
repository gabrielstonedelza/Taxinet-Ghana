# Generated by Django 4.0.3 on 2023-03-02 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxinet_api', '0026_alter_userrequesttopup_top_up_option'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drivervehicleinventory',
            name='registration_number',
        ),
        migrations.RemoveField(
            model_name='drivervehicleinventory',
            name='unique_number',
        ),
        migrations.RemoveField(
            model_name='drivervehicleinventory',
            name='vehicle_brand',
        ),
        migrations.AddField(
            model_name='drivervehicleinventory',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
