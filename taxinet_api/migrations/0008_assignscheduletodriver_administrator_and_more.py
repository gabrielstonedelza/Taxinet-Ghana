# Generated by Django 4.0.3 on 2022-07-27 08:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taxinet_api', '0007_contactus'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignscheduletodriver',
            name='administrator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='scheduleride',
            name='assigned_driver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='driver_to_be_assigned', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='completedbidonscheduledride',
            name='administrator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Administrator_completing_scheduled_ride', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ContactAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]