from django.db import models

class Car(models.Model):
    matricule = models.CharField(max_length=10 , primary_key=True)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='', blank=True, null=True)
    status = models.CharField(max_length=20, choices=[('Disponible','Disponible'), ('Indisponible', 'Indisponible')], default='Disponible')
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
    description = models.CharField(max_length=255 , default='Pas de description')


    
    def _str_(self):
        return f"{self.brand} {self.model} - {self.year}"

class Client(models.Model):
    cin = models.CharField(primary_key=True ,max_length=10)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    
    def _str_(self):
        return self.username

class Manager(models.Model):
    cin = models.CharField(primary_key=True ,max_length=10)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    
    def _str_(self):
        return self.username



class Reservation(models.Model):
    N_Serie = models.AutoField(primary_key=True)
    car = models.ForeignKey(Car , on_delete=models.CASCADE)
    client = models.ForeignKey(Client , on_delete=models.CASCADE)
    reservation_date = models.DateField(auto_now_add=True)
    status_choices = [('En attente', 'En attente'),('Accepte', 'Accepte'),('Rejete', 'Rejete'),]
    status = models.CharField(max_length=20, choices=status_choices, default='En attente')

    def _str_(self):
        return f"Reservation for {self.car} by {self.client}"

    
class Administrator(models.Model):
    cin = models.CharField(primary_key=True ,max_length=10)
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def _str_(self):
        return self.username