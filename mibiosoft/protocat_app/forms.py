from django import forms
from .models import UserRegistration, UserAuthentication, Protocol
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.forms import ModelForm, PasswordInput
from django_comments.forms import CommentForm
from django_comments.models import Comment
import operator

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
    title = forms.CharField(widget=forms.Textarea(attrs={'rows':1, 'cols':60}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows':5, 'cols':40}))
    protocol_steps = forms.CharField(required=False)
    class Meta:
        model = Protocol
        fields = ['title','description','protocol_type', 'reagents','protocol_steps']
        exclude = [None]

