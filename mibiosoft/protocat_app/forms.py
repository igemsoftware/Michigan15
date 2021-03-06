from django import forms
from .models import UserRegistration, UserAuthentication, Protocol
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.forms import ModelForm, PasswordInput
from django_comments.forms import CommentForm
from django_comments.models import Comment
from .protocols import PROTOCOL_TYPES
import operator

'''
Add your forms here
For default Django format, add your fields under "field" in the metaclass
If you want to customize your field format, do so outside the metaclass
'''

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        widgets = {
            'password' : PasswordInput(),
        }
        fields = ['user_name', 'first_name', 'last_name', 'email', 'password']
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
    reagents = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows':10, 'cols':30}))
    protocol_type = forms.ChoiceField(required=False, choices=PROTOCOL_TYPES)

    class Meta:
        model = Protocol
        fields = ['title','description','protocol_type', 'reagents','protocol_steps']
        exclude = [None]



