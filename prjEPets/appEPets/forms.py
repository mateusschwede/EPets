from django import forms
from django.forms import ModelForm
from .models import *

class FormPet(forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'