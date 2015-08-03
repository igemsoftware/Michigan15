from django import forms
from .models import UserRegistration, UserAuthentication, Protocol
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.forms import ModelForm, PasswordInput

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        widgets = {
            'password' : PasswordInput(),
        }
        fields = ['user_name', 'email', 'password']
        exclude = [None]

class UserAuthenticationForm(forms.ModelForm):
    class Meta:
        model = UserAuthentication
        widgets = {
            'password' : PasswordInput(),
        }
        fields = ['user_name', 'password']
        exclude = [None]

class ProtocolUploadForm(forms.ModelForm):
    class Meta:
        model = Protocol
        fields = ['title', 'description', 'protocol_type', 'reagents']
        exclude = [None]