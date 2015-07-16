from django import forms
from .models import UserRegistration, UserAuthentication, ProtocolUpload
from django.core.exceptions import ValidationError
from django.utils import timezone


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = ['user_name', 'email', 'password']
        exclude = [None]

class UserAuthenticationForm(forms.ModelForm):
    date_of_upload = timezone.now()
    class Meta:
        model = UserAuthentication
        fields = ['user_name', 'password']
        exclude = [None]

class ProtocolUploadForm(forms.ModelForm):

    class Meta:
        model = ProtocolUpload
        fields = ['title', 'protocol_type', 'rating', 'protocol']
        exclude = [None]