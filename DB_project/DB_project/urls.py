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
from django.conf import settings
from django.conf.urls.static import static
from appCar.views import home, ajouter_voiture,dashboard,our_managers,our_admins,modifier_manager,supprimer_manager,ajouter_manager,dashboard_manager,login_view,logout_view,our_clients,our_cars,our_reservations, ajouter_admin , view_car,modifier_client,supprimer_client,ajouter_client,supprimer_car,modifier_car,supprimer_reservation,admin_info,manager_info,accepter_reservation,refuser_reservation



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', login_view , name='login_view'),
    path('logout/', logout_view, name='logout'),
    path('admin_dashboard/', dashboard, name='admin_dashboard'),
    path('dashboard_manager/', dashboard_manager, name='dashboard_manager'),
    path('our-managers/', our_managers, name='our_managers'),
    path('our-admins/', our_admins, name='our_admins'),
    path('our-clients/', our_clients, name='our_clients'),
    path('our-cars/', our_cars, name='our_cars'),
    path('view-car/<str:matricule>', view_car, name='view_car'),
    path('ajouter_voiture/', ajouter_voiture, name='ajouter_voiture'),  
    path('our-reservations/', our_reservations, name='our_reservations'),
    # URL pour la modification d'un gestionnaire
    path('modifier-manager/<str:manager_cin>/', modifier_manager, name='modifier_manager'),
    path('modifier-client/<str:client_cin>', modifier_client, name='modifier_client'),
    #modifier voiture
    path('modifier-car/<str:matricule>/', modifier_car, name='modifier_car'),
    # URL pour la suppression d'un gestionnaire
    path('supprimer-manager/<str:manager_cin>/', supprimer_manager, name='supprimer_manager'),
    #supprimer client
    path('supprimer-client/<str:client_cin>/', supprimer_client, name='supprimer_client'),
    #supprimer voiture
    path('supprimer-car/<str:matricule>/', supprimer_car, name='supprimer_car'),
    #supprimer reservation
    path('supprimer-reservation/<int:id>/', supprimer_reservation, name='supprimer_reservation'),
    #ajouter manager
    path('ajouter-manager/', ajouter_manager, name='ajouter_manager'),
    path('ajouter-admin/', ajouter_admin, name='ajouter_admin'),
    #ajouter client
    path('ajouter-client/', ajouter_client, name='ajouter_client'),
    #admin info
    path('admin-info/<str:cin>/' , admin_info , name='admin_info'),
    path('manager-info/<str:cin>/' , manager_info , name='manager_info'),
    #accpter reservation
    path('accepter-reservation/<int:id>/', accepter_reservation, name='accepter_reservation'),
    #refuser reservation
    path('refuser-reservation/<int:id>/', refuser_reservation, name='refuser_reservation'),



   
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)