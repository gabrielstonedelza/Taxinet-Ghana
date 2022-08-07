# Generated by Django 4.0.3 on 2022-08-06 09:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taxinet_api', '0011_alter_messages_date_sent_alter_messages_time_sent'),
    ]

    operations = [
        migrations.CreateModel(
            name='AskToLoadWallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10)),
                ('date_requested', models.DateTimeField(auto_now_add=True)),
                ('administrator', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='administrator', to=settings.AUTH_USER_MODEL)),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CompletedScheduledRidesToday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10)),
                ('date_completed', models.DateTimeField(auto_now_add=True)),
                ('scheduled_ride', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taxinet_api.scheduleride')),
            ],
        ),
        migrations.CreateModel(
            name='PassengersWallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10)),
                ('date_loaded', models.DateTimeField(auto_now_add=True)),
                ('administrator', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='administrator_for_wallet', to=settings.AUTH_USER_MODEL)),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passengers_wallet', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='completedbidonscheduledride',
            name='administrator',
        ),
        migrations.RemoveField(
            model_name='completedbidonscheduledride',
            name='scheduled_ride',
        ),
        migrations.RemoveField(
            model_name='completedscheduledrides',
            name='scheduled_ride',
        ),
        migrations.RemoveField(
            model_name='messages',
            name='ride',
        ),
        migrations.RemoveField(
            model_name='messages',
            name='user',
        ),
        migrations.DeleteModel(
            name='BidScheduleRide',
        ),
        migrations.DeleteModel(
            name='CompletedBidOnScheduledRide',
        ),
        migrations.DeleteModel(
            name='CompletedScheduledRides',
        ),
        migrations.DeleteModel(
            name='Messages',
        ),
    ]