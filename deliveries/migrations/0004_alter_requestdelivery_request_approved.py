# Generated by Django 4.0.3 on 2023-11-17 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deliveries', '0003_remove_requestdelivery_items_delivering_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestdelivery',
            name='request_approved',
            field=models.CharField(default='Pending', max_length=30),
        ),
    ]
