# Generated by Django 4.0.3 on 2024-05-19 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_for_rent', '0006_carsforrent_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='carsforrent',
            name='drive_type',
            field=models.CharField(choices=[('Self Drive', 'Self Drive'), ('With a Driver', 'With a Driver')], default='With a Driver', max_length=50),
        ),
        migrations.AddField(
            model_name='carsforrent',
            name='k200',
            field=models.CharField(default='Ghc900', max_length=20),
        ),
        migrations.AddField(
            model_name='carsforrent',
            name='k300',
            field=models.CharField(default='Ghc1000', max_length=20),
        ),
        migrations.AddField(
            model_name='carsforrent',
            name='k400',
            field=models.CharField(default='Ghc1200', max_length=20),
        ),
        migrations.AddField(
            model_name='carsforrent',
            name='k500',
            field=models.CharField(default='Ghc1300', max_length=20),
        ),
        migrations.AddField(
            model_name='carsforrent',
            name='k600',
            field=models.CharField(default='Ghc1400', max_length=20),
        ),
        migrations.AddField(
            model_name='carsforrent',
            name='kk200',
            field=models.CharField(default='Ghc700', max_length=20),
        ),
        migrations.AddField(
            model_name='carsforrent',
            name='outside_ksi',
            field=models.BooleanField(default=False),
        ),
    ]