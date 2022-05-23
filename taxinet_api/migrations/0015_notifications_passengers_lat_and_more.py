# Generated by Django 4.0.3 on 2022-05-23 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxinet_api', '0014_notifications_drop_off_place_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='passengers_lat',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='notifications',
            name='passengers_lng',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='requestride',
            name='passengers_lat',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='requestride',
            name='passengers_lng',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
