# Generated by Django 4.1.13 on 2024-04-23 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('cin', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('matricule', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.CharField(blank=True, max_length=255)),
                ('status', models.CharField(choices=[('Available', 'Available'), ('Unavailable', 'Unavailable')], default='Available', max_length=20)),
                ('fuel', models.CharField(blank=True, max_length=255)),
                ('kilometer', models.IntegerField()),
                ('seats', models.IntegerField(default=2)),
                ('air_conditioning', models.BooleanField(default=False)),
                ('child_seat', models.BooleanField(default=False)),
                ('gps', models.BooleanField(default=False)),
                ('music', models.BooleanField(default=False)),
                ('seat_belt', models.BooleanField(default=False)),
                ('sleeping_bed', models.BooleanField(default=False)),
                ('bluetooth', models.BooleanField(default=False)),
                ('onboard_computer', models.BooleanField(default=False)),
                ('audio_input', models.BooleanField(default=False)),
                ('car_kit', models.BooleanField(default=False)),
                ('climate_control', models.BooleanField(default=False)),
                ('description', models.CharField(default='No description', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('cin', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('cin', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=True)),
                ('reservation_date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending', max_length=20)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appCar.car')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appCar.client')),
            ],
        ),
    ]
