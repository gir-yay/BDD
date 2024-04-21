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
        brands = ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'BMW']
        for _ in range(10):  # Generate 10 cars
            price = round(random.uniform(10000, 50000), 2)
            Car.objects.create(
                registration_number=fake.random_int(min=1000, max=9999),
                brand=random.choice(brands),
                model=fake.word(),
                year=fake.random_int(min=2000, max=2024),
                price=price,
                image=fake.image_url(),
                status=random.choice(['Available', 'Unavailable']),
                fuel=random.choice(['Petrol', 'Diesel', 'Electric']),
                kilometer=fake.random_int(min=1000, max=100000),
                seats=fake.random_int(min=2, max=7),
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
        for _ in range(5):  # Generate 5 clients
            Client.objects.create(
                name=fake.name(),
                email=fake.email(),
                phone=fake.phone_number(),
            )

    def generate_managers(self):
        for _ in range(2):  # Generate 2 managers
            Manager.objects.create(
                name=fake.name(),
                username=fake.user_name(),
                phone=fake.phone_number(),
                email=fake.email(),
                password="12345",
            )

    def generate_reservations(self):
        cars = Car.objects.all()
        clients = Client.objects.all()
        managers = Manager.objects.all()
        for _ in range(10):  # Generate 10 reservations
            Reservation.objects.create(
                car=random.choice(cars),
                client=random.choice(clients),
                manager=random.choice(managers),
                status=random.choice(['Pending', 'Accepted', 'Rejected']),
            )

    def generate_admins(self):
        Administrator.objects.create(
            username=fake.user_name(),
            password="12345",
        )
