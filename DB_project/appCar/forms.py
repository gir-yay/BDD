from django import forms
from .models import Car
from .models import Manager
from .models import Administrator
from .models import Client


class VoitureForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__' 

class ManagerForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = '__all__'  


class AdminForm(forms.ModelForm):
    class Meta:
        model = Administrator
        fields = '__all__'  


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'