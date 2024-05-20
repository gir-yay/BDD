from datetime import datetime, timedelta
from celery import shared_task
from .models import Car, Reservation

@shared_task
def update_car_availability():
    today = datetime.now().date()
    accepted_reservations = Reservation.objects.filter(status='Accepte')  # Filter accepted reservations
    for reservation in accepted_reservations:
        end_date = reservation.starting_date + timedelta(days=reservation.period)
        if end_date == today:
            car = reservation.car
            car.status = 'Disponible'  
            car.save()
            
@shared_task
def update_car_unavailability():
    today = datetime.now().date()
    accepted_reservations = Reservation.objects.filter(status='Accepte')  # Filter accepted reservations
    for reservation in accepted_reservations:
        if reservation.starting_date == today:
            car = reservation.car
            car.status = 'Indisponible'  
            car.save()
            
#commmands to run
#celery -A DB_project beat -l INFO
#celery -A DB_project worker -l INFO
