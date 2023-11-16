# Generated by Django 4.0.3 on 2023-11-15 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApprovedSchedules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.scheduleride')),
            ],
        ),
    ]