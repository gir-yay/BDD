from django import forms
from .models import Car
from .models import Manager
from .models import Administrator


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