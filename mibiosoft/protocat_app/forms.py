from django import forms
from .models import UserRegistration, UserAuthentication, Protocol
from django.core.exceptions import ValidationError
from django.utils import timezone


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = ['user_name', 'email', 'password']
        exclude = [None]

class UserAuthenticationForm(forms.ModelForm):
    class Meta:
        model = UserAuthentication
        fields = ['user_name', 'password']
        exclude = [None]

class ProtocolUploadForm(forms.ModelForm):
    class Meta:
        model = Protocol
        fields = ['title', 'description', 'protocol_type', 'reagents', 'protocol']
        exclude = [None]

