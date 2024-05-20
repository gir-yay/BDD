# celery.py

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DB_project.settings')

app = Celery('DB_project')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'update-car-availability': {
        'task': 'appCar.tasks.update_car_availability',
        'schedule': crontab(hour=0, minute=0),  # Run daily at midnight
    },
    'update-car-unavailability': {
        'task': 'appCar.tasks.update_car_unavailability',
        'schedule': crontab(hour=0, minute=0),  # Run daily at midnight
    },
    # Add more periodic tasks as needed
}
