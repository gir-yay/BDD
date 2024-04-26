
from django.shortcuts import render, redirect
from .forms import VoitureForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Manager
from .models import Administrator
from .models import Reservation
from .models import Car
from .models import Client
from django.shortcuts import  get_object_or_404
from .forms import ManagerForm 
from .decorators import is_manager
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from pymongo import MongoClient
from .forms import AdminForm

# Configuration de la connexion à MongoDB
client = MongoClient('localhost', 27017)
db = client['locationv_db']


def home(request):
    cars = Car.objects.all()[:6]
    return render(request, 'home.html' , {'cars': cars})



def authenticate_manager(username, password):
    manager_collection = db['appCar_manager']
    manager = manager_collection.find_one({'username': username, 'password': password})
    return manager is not None

def authenticate_admin(username, password):
    admin_collection = db['appCar_administrator']
    admin = admin_collection.find_one({'username': username, 'password': password})
    return admin is not None





def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        is_manager = authenticate_manager(username, password)
        is_admin = authenticate_admin(username, password)
        
        if is_manager:

            return redirect('dashboard_manager')
        elif is_admin:
            return redirect('admin_dashboard')
        else:
            return render(request, 'login.html', {'error': 'Identifiants invalides'})
    else:
        return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('home')



##########################################################
    #admin dashboard


def dashboard(request):
    # Nombre total de clients
    
    total_clients = Client.objects.count()

    # Nombre total de voitures
    total_voitures = Car.objects.count()

    # Nombre total de réservations
    total_reservations = Reservation.objects.count()

    context = {
        'total_clients': total_clients,
        'total_voitures': total_voitures,
        'total_reservations': total_reservations,
    }
    
    return render(request, 'admin_dashboard.html', context)


#===== dashboard manager

def dashboard_manager(request):
    # Nombre total de clients
    
    total_clients = Client.objects.count()

    # Nombre total de voitures
    total_voitures = Car.objects.count()

    # Nombre total de réservations
    total_reservations = Reservation.objects.count()

    context = {
        'total_clients': total_clients,
        'total_voitures': total_voitures,
        'total_reservations': total_reservations,
    }
    return render(request, 'manager_dashboard.html' , context)


#===================================================================================================================================
#our manager ( consultation des manages par le admin)

def our_managers(request):
    managers = Manager.objects.all()
    return render(request, 'our_managers.html', {'managers': managers})


def our_admins(request):
    administrators = Administrator.objects.all()
    return render(request, 'our_admins.html', {'administrators': administrators})


def our_clients(request):
    clients = Client.objects.all()
    return render(request, 'our_clients.html', {'clients': clients})


def our_cars(request):
    cars = Car.objects.all()
    return render(request, 'our_cars.html', {'cars': cars})


    

def our_reservations(request):
    reservations = Reservation.objects.all()
    return render(request, 'our_reservations.html', {'reservations': reservations})

#===================================================================================================================================
#modifier un manager

def modifier_manager(request, manager_cin):
    manager = get_object_or_404(Manager, pk=manager_cin)
    if request.method == 'POST':
        form = ManagerForm(request.POST, instance=manager)
        if form.is_valid():
            form.save()
            return redirect('our_managers')  # Rediriger vers le tableau de bord après modification
    else:
        form = ManagerForm(instance=manager)
    return render(request, 'modifier_manager.html', {'form': form})

#===================================================================================================================================
#suprimer manager

def supprimer_manager(request, manager_cin):
    manager = get_object_or_404(Manager, pk=manager_cin)
    if request.method == 'POST':
        # Supprimer le manager uniquement si la méthode est POST
        manager.delete()
        return redirect('our_managers')
    else:
        # Rediriger vers une page d'erreur ou une autre vue si la méthode n'est pas POST
        return redirect('page_d_erreur')
    
#===================================================================================================================================
    # ajouter un manager
def ajouter_manager(request):
    if request.method == 'POST':
        form = ManagerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('our_managers')  # Rediriger vers le tableau de bord après l'ajout
    else:
        form = ManagerForm()
    return render(request, 'ajouter_manager.html', {'form': form})

def ajouter_admin(request):
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('our_admins')  # Rediriger vers le tableau de bord après l'ajout
    else:
        form = AdminForm()
    return render(request, 'ajouter_admin.html', {'form': form})


def ajouter_voiture(request):
    if request.method == 'POST':
        form = VoitureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Rediriger vers la page d'accueil après l'ajout
    else:
        form = VoitureForm()
    return render(request, 'ajouter_voiture.html', {'form': form})


