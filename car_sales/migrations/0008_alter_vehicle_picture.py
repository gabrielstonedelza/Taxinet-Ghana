# Generated by Django 4.0.3 on 2024-03-12 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_sales', '0007_rename_milage_vehicle_millage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='picture',
            field=models.ImageField(default='taxinet_cab.png', upload_to='cars_initial_pics'),
        ),
    ]
