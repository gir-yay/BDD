# Generated by Django 4.1.13 on 2024-04-29 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appCar', '0003_alter_car_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
