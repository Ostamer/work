# forms.py
from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'phone_number']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ваше имя', 'class': 'input_field'}),
            'phone_number': forms.TextInput(attrs={'placeholder': '+7 (999) 999-99-99', 'class': 'phone_field'}),
        }
