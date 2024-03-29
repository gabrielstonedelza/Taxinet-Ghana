# Generated by Django 4.0.3 on 2023-11-14 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airline', models.CharField(choices=[('Africa World Airlines', 'Africa World Airlines'), ('PassionAir', 'PassionAir'), ('Hour', 'Hour')], default='PassionAir', max_length=100)),
                ('departure_airport', models.CharField(choices=[('Kumasi Airport (KSI)', 'Kumasi Airport (KSI)'), ('Accra (ACC)', 'Kumasi Airport (KSI)Accra (ACC)')], default='Kumasi Airport (KSI)', max_length=100)),
                ('arrival_airport', models.CharField(choices=[('Kumasi Airport (KSI)', 'Kumasi Airport (KSI)'), ('Accra (ACC)', 'Kumasi Airport (KSI)Accra (ACC)')], default='Kumasi Airport (KSI)', max_length=100)),
                ('flight_type', models.CharField(choices=[('Round Trip', 'Round Trip'), ('One Way', 'One Way')], default='Round Trip', max_length=100)),
                ('departure_date', models.CharField(max_length=20)),
                ('departure_time', models.CharField(max_length=20)),
                ('returning_date', models.CharField(blank=True, max_length=20)),
                ('returning_time', models.CharField(blank=True, max_length=20)),
                ('flight_booked', models.BooleanField(default=False)),
                ('date_booked', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
