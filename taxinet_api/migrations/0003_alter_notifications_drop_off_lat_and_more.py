# Generated by Django 4.0.3 on 2022-06-27 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxinet_api', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='drop_off_lat',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='drop_off_lng',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
