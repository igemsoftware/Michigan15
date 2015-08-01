from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import ModelForm, PasswordInput
from datetime import datetime
from .protocols import PROTOCOL_TYPES
from django.contrib.auth.models import User


class UserRegistration(models.Model):
    email = models.EmailField(blank=False)
    user_name = models.CharField(max_length=50, default='First Last', blank=False)
    password = models.CharField(max_length=120, default='password', blank=False)

    def __str__(self):
        return (self.user_name + ', ' + self.email)

class UserAuthentication(models.Model):
    user_name = models.CharField(max_length=50, default='YourUserName')
    password = models.CharField(max_length=120, default='password', blank=False)

    def __str__(self):
        return (self.user_name + ', ' + self.email)


# class Protocol(models.Model):
#     title = models.TextField()
#     # author = ... TODO: tie in with user permissions etc.
#     date_of_upload = models.DateField
#     protocol_type = models.CharField(max_length=2, choices=PROTOCOL_TYPES, null=True)
#     rating = models.DecimalField(
#         validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
#         max_digits=3, decimal_places=2, default = 0.00)
#     protocol = models.TextField(default = '')




class Protocol(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    author = models.CharField(max_length=50)
    date_of_upload = datetime.now()
    description = models.TextField(default='')
    protocol_type = models.CharField(max_length=2, choices=PROTOCOL_TYPES, null=True)
    rating = models.DecimalField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
        max_digits=3, decimal_places=2, default=2.50)
    num_ratings = models.IntegerField(default=0)
    user_rated = models.TextField(default='')
    reagents = models.TextField(default='')
    protocol_steps = models.TextField(default='')

