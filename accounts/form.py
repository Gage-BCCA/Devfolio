from django.forms import ModelForm
from django import forms
from .models import *

class CreateAccount(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    password2=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Account
        fields = '__all__'