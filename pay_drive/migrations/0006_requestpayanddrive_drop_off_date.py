# Generated by Django 4.0.3 on 2024-03-14 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay_drive', '0005_paydailypayanddrive'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestpayanddrive',
            name='drop_off_date',
            field=models.CharField(default='', max_length=10),
        ),
    ]