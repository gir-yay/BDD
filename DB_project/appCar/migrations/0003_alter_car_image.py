# Generated by Django 4.1.13 on 2024-04-29 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appCar', '0002_alter_car_image_alter_reservation_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]