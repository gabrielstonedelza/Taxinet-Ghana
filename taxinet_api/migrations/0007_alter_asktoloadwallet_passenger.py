# Generated by Django 4.0.3 on 2022-08-26 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taxinet_users', '0001_initial'),
        ('taxinet_api', '0006_alter_asktoloadwallet_passenger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asktoloadwallet',
            name='passenger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taxinet_users.passengerprofile'),
        ),
    ]
