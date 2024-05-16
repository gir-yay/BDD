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
            car.status = 'Disponible'  # Assuming 'Disponible' means available
            car.save()
            

#commmands to run
#celery -A your_project beat -l INFO
#celery -A your_project worker -l INFO
