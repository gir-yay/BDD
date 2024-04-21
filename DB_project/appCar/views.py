
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


def home(request):
    return render(request, 'home.html')


def ajouter_voiture(request):
    if request.method == 'POST':
        form = VoitureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Rediriger vers la page d'accueil après l'ajout
    else:
        form = VoitureForm()
    return render(request, 'ajouter_voiture.html', {'form': form})
#""""""""""""""""""""""""""""""""""""
#===================================================================================================================================
#login manager

""""
def manager_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        manager = authenticate(request, email=email, password=password)

        if manager is not None:
            login(request, manager)
            return redirect('dashboard_manager')  # Rediriger vers la page du tableau de bord des managers
        else:
            # Afficher un message d'erreur en cas d'informations d'identification incorrectes
            error_message = "Invalid email or password. Please try again."
            return render(request, 'manager_login.html', {'error_message': error_message})
    else:
        return render(request, 'manager_login.html')
    """

    #"""""""""""""""""""""""""""""""""""""
#===================================================================================================================================
    #admin login 
"""
def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
       # user.is_superuser
        
            login(request, user)
            return redirect('admin_dashboard')  # Rediriger vers le tableau de bord de l'administrateur
        else:
            # Afficher un message d'erreur en cas d'informations d'identification incorrectes
            error_message = "Invalid username or password. Please try again."
           # messages.error(request, error_message)
            return render(request,'admin_login.html', {'error_message': error_message})  # Rediriger vers la page de connexion de l'administrateur
    else:
        return render(request, 'admin_login.html')
"""
    #""""""""""""""""""""""""""""""""""""""""""""""""
#===================================================================================================================================
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
#"""""""""""""""""""""""""""""""""""
#===================================================================================================================================
#our manager ( consultation des manages par le admin)

def our_managers(request):
    managers = Manager.objects.all()
    return render(request, 'our_managers.html', {'managers': managers})

#""""""""""""""""""""""""""""""""
#===================================================================================================================================
#modifier un manager

def modifier_manager(request, manager_id):
    manager = get_object_or_404(Manager, pk=manager_id)
    if request.method == 'POST':
        form = ManagerForm(request.POST, instance=manager)
        if form.is_valid():
            form.save()
            return redirect('our_managers')  # Rediriger vers le tableau de bord après modification
    else:
        form = ManagerForm(instance=manager)
    return render(request, 'modifier_manager.html', {'form': form})
#""""""""""""""""""""""""""""""""""""""
#===================================================================================================================================
#suprimer manager

def supprimer_manager(request, manager_id):
    manager = get_object_or_404(Manager, pk=manager_id)
    if request.method == 'POST':
        # Supprimer le manager uniquement si la méthode est POST
        manager.delete()
        return redirect('our_managers')
    else:
        # Rediriger vers une page d'erreur ou une autre vue si la méthode n'est pas POST
        return redirect('page_d_erreur')
    #""""""""""""""""""""""""""""
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
 #""""""""""""""""""""""""""""
#===== dashboard manager
   
def dashboard_manager(request):
   

    return render(request, 'manager_dashboard.html')


from pymongo import MongoClient

def authenticate_manager(username, password):
    manager_collection = db['appCar_manager']
    manager = manager_collection.find_one({'username': username, 'password': password})
    return manager is not None

def authenticate_admin(username, password):
    admin_collection = db['appCar_administrator']
    admin = admin_collection.find_one({'username': username, 'password': password})
    return admin is not None


# Configuration de la connexion à MongoDB
client = MongoClient('localhost', 27017)
db = client['locationv_db']

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
