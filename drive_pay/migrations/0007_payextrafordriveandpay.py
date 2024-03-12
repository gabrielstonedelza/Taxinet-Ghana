# Generated by Django 4.0.3 on 2024-03-12 17:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('drive_pay', '0006_lockcarfortheday'),
    ]

    operations = [
        migrations.CreateModel(
            name='PayExtraForDriveAndPay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=19)),
                ('date_paid', models.DateTimeField(auto_now_add=True)),
                ('approved_drive', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drive_pay.addtoapproveddriveandpay')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_daily_drive', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
