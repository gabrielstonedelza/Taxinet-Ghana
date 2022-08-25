# Generated by Django 4.0.3 on 2022-08-25 08:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taxinet_users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddToVerified',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_verified', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='verified_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]