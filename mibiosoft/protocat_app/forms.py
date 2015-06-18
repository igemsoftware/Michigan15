from django import forms
from .models import SignUp

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name','email']

    def clean_email(self):
        email = (self.cleaned_data.get('email'))
        # if you want to exclude certain emails:
        # email_base, provider = email.split('@')
        # domain, extension = provider.split('.')
        # if not extension == 'edu':
        #     raise forms.ValidationError('Please use a valid .edu email address')
        return email

class ContactFrom(forms.Form):
    full_name= forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()
