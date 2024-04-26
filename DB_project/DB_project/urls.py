"""DB_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appCar.views import home, ajouter_voiture,dashboard,our_managers,our_admins,modifier_manager,supprimer_manager,ajouter_manager,dashboard_manager,login_view,logout_view,our_clients,our_cars,our_reservations, ajouter_admin



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('ajouter_voiture/', ajouter_voiture, name='ajouter_voiture'), 
    path('login/', login_view , name='login_view'),
    path('logout/', logout_view, name='logout'),
    path('admin_dashboard/', dashboard, name='admin_dashboard'),
    path('dashboard_manager/', dashboard_manager, name='dashboard_manager'),
    path('our-managers/', our_managers, name='our_managers'),
    path('our-admins/', our_admins, name='our_admins'),
    path('our-clients/', our_clients, name='our_clients'),
    path('our-cars/', our_cars, name='our_cars'),
    path('our-reservations/', our_reservations, name='our_reservations'),
    # URL pour la modification d'un gestionnaire
    path('modifier-manager/<str:manager_cin>/', modifier_manager, name='modifier_manager'),
    # URL pour la suppression d'un gestionnaire
    path('supprimer-manager/<str:manager_cin>/', supprimer_manager, name='supprimer_manager'),
    path('ajouter-manager/', ajouter_manager, name='ajouter_manager'),
    path('ajouter-admin/', ajouter_admin, name='ajouter_admin'),

   
    

]
