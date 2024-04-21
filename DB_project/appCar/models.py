from django.db import models

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    registration_number = models.CharField(max_length=10)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=20, choices=[('Available', 'Available'), ('Unavailable', 'Unavailable')], default='Available')
    fuel = models.CharField(max_length=255, blank=True)
    kilometer =models.IntegerField()
    seats = models.IntegerField(default=2)
    air_conditioning = models.BooleanField(default=False)
    child_seat = models.BooleanField(default=False)
    gps = models.BooleanField(default=False)
    music = models.BooleanField(default=False)
    seat_belt = models.BooleanField(default=False)
    sleeping_bed = models.BooleanField(default=False)
    bluetooth = models.BooleanField(default=False)
    onboard_computer = models.BooleanField(default=False)
    audio_input = models.BooleanField(default=False)
    car_kit = models.BooleanField(default=False)
    climate_control = models.BooleanField(default=False)
    description = models.CharField(max_length=255 , default='No description')


    
    def _str_(self):
        return f"{self.brand} {self.model} - {self.year}"

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    
    def _str_(self):
        return self.username

class Manager(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    
    def _str_(self):
        return self.username



class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    car = models.ForeignKey(Car , on_delete=models.CASCADE)
    client = models.ForeignKey(Client , on_delete=models.CASCADE)
    manager = models.ForeignKey(Manager , on_delete=models.CASCADE)
    reservation_date = models.DateField(auto_now_add=True)
    status_choices = [('Pending', 'Pending'),('Accepted', 'Accepted'),('Rejected', 'Rejected'),]
    status = models.CharField(max_length=20, choices=status_choices, default='Pending')

    def _str_(self):
        return f"Reservation for {self.car} by {self.username}"

    
class Administrator(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def _str_(self):
        return self.username