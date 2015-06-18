from django.contrib import admin
from .models import SignUp
from .forms import SignUpForm

class SignUpAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'timestamp', 'updated']
    form = SignUpForm

admin.site.register(SignUp)
