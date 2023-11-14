# Generated by Django 4.0.3 on 2023-11-14 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RequestDriveAndPay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.CharField(max_length=100)),
                ('period', models.CharField(max_length=10)),
                ('pick_up_date', models.CharField(max_length=10)),
                ('drop_off_date', models.CharField(max_length=10)),
                ('period_total_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=19)),
                ('request_approved', models.BooleanField(default=False)),
                ('date_requested', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
