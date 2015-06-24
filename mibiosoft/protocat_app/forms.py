from django import forms
from .models import UserRegistration, UserAuthentication
from django.core.exceptions import ValidationError

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = ['user_name', 'email', 'password']
        exclude = [None]

class UserAuthenticationForm(forms.ModelForm):
    class Meta:
        model = UserAuthentication
        fields = ['user_name', 'password']
        exlcude = [None]