# Generated by Django 4.0.3 on 2024-04-03 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay_drive', '0009_addtoapprovedpayanddrive_expired'),
    ]

    operations = [
        migrations.AddField(
            model_name='addtoapprovedpayanddrive',
            name='dropped_off',
            field=models.BooleanField(default=False),
        ),
    ]
