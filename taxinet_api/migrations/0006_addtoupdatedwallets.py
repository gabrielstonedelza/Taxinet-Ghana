# Generated by Django 4.0.3 on 2022-08-24 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taxinet_api', '0005_rename_schedule_ride_id_schedulednotifications_schedule_ride_slug_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddToUpdatedWallets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taxinet_api.passengerswallet')),
            ],
        ),
    ]