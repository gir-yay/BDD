import random
from django.core.management.base import BaseCommand
from faker import Faker
from appCar.models import Car, Client, Manager, Reservation, Administrator

fake = Faker()

class Command(BaseCommand):
    help = 'Generate dummy data for MongoDB database'

    def handle(self, *args, **kwargs):
        self.generate_cars()
        self.generate_clients()
        self.generate_managers()
        self.generate_reservations()
        self.generate_admins()
        self.stdout.write(self.style.SUCCESS('Dummy data generated successfully'))

    def generate_cars(self):
        cars_list = [
            {'brand': 'Marcedes', 'model': 'Benz', 'image': 'car-1.jpeg'},
            {'brand': 'Marcedes', 'model': 'Amg', 'image': 'car-2.jpeg'},
            {'brand': 'Peugeot', 'model': '108', 'image': 'car-3.jpg'},
            {'brand': 'Citroen', 'model': 'C5 Aircross', 'image': 'car-4.jpeg'},
            {'brand': 'Dacia', 'model': 'Sandero', 'image': 'car-5.jpeg'},
            {'brand': 'Dacia', 'model': 'Logan', 'image': 'car-6.jpg'},
            {'brand': 'Dacia', 'model': 'Duster', 'image': 'car-7.jpeg'},
            {'brand': 'Renault', 'model': 'Kangoo', 'image': 'car-8.jpg'},
            {'brand': 'Seat', 'model': 'Ibiza', 'image': 'car-9.jpeg'},
            {'brand': 'Seat', 'model': 'Nuevo Alhambra', 'image': 'car-10.jpg'}
        ]

        for car_info in cars_list:  # Generate 10 cars
            Car.objects.create(
                matricule=fake.random_int(min=10000, max=99999),
                brand=car_info['brand'],
                model=car_info['model'],
                year=fake.random_int(min=2021, max=2023),
                price=fake.random_int(min=500, max=1000),
                image=car_info['image'],
                status=random.choice(['Disponible', 'Indisponible']),
                fuel=random.choice(['Pétrole', 'Diesel', 'Eléctrique', 'Hybride']),
                kilometer=fake.random_int(min=1000, max=8000),
                seats=fake.random_int(min=2, max=6),
                air_conditioning=fake.boolean(),
                child_seat=fake.boolean(),
                gps=fake.boolean(),
                music=fake.boolean(),
                seat_belt=fake.boolean(),
                sleeping_bed=fake.boolean(),
                bluetooth=fake.boolean(),
                onboard_computer=fake.boolean(),
                audio_input=fake.boolean(),
                car_kit=fake.boolean(),
                climate_control=fake.boolean(),
                description=fake.text(),
            )
    

    def generate_clients(self):
        cin_ = ['EE123456', 'LC654321', 'BC987654', 'AC456789', 'MM321654']
        for _ in range(5):  # Generate 5 clients
            Client.objects.create(
                cin =cin_[_],
                name=fake.name(),
                email=fake.email(),
                phone=fake.phone_number(),
            )

    def generate_managers(self):
        cin_ = ['EE188456', 'MM67721']
        for _ in range(2):  # Generate 2 managers
            Manager.objects.create(
                cin =cin_[_],
                name=fake.name(),
                username=fake.user_name(),
                phone=fake.phone_number(),
                email=fake.email(),
                password="12345",
            )

    def generate_reservations(self):
        cars = Car.objects.all()
        clients = Client.objects.all()
        for _ in range(10):  # Generate 10 reservations
            Reservation.objects.create(
                car=random.choice(cars),
                client=random.choice(clients),
                starting_date = fake.date_between(start_date='-1y', end_date='+1y'),
                period = fake.random_int(min=1, max=7),
                status=random.choice(['En attente', 'Accepte', 'Rejete']),
            )

    def generate_admins(self):
        Administrator.objects.create(
            cin ='BN789564' ,
            username='admin',
            name=fake.name(),
            phone=fake.phone_number(),
            email=fake.email(),
            password="12345",
        )
