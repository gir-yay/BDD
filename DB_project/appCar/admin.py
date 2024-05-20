

# Register your models here.
from django.contrib import admin
from .models import Manager, Administrator,Client,Car

admin.site.register(Manager)
admin.site.register(Administrator)
admin.site.register(Client)
admin.site.register(Car)

