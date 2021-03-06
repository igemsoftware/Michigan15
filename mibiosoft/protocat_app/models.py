from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import ModelForm, PasswordInput
from datetime import datetime
from .protocols import PROTOCOL_TYPES
from django.contrib.auth.models import User
from django_comments.forms import CommentForm
from django_comments.models import Comment
from django.db.models import Q

'''
Add your models here
'''


class UserRegistration(models.Model):
    email = models.EmailField(blank=False)
    first_name = models.CharField(max_length=20, default='')
    last_name = models.CharField(max_length=20, default='')
    user_name = models.CharField(max_length=50, default='First Last', blank=False)
    password = models.CharField(max_length=120, default='password', blank=False)

    def __str__(self):
        return (self.user_name + ', ' + self.email)
    def details(self):
        return self.user_name + ', ' + self.email


class UserAuthentication(models.Model):
    user_name = models.CharField(max_length=50, default='YourUserName')
    password = models.CharField(max_length=120, default='password', blank=False)

    def __str__(self):
        return (self.user_name + ', ' + self.email)
    def details(self):
        return self.user_name + ', ' + self.password


class Protocol(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    author = models.CharField(max_length=50)
    date_of_upload = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    description = models.TextField(blank=True)
    protocol_type = models.CharField(max_length=2, choices=PROTOCOL_TYPES, null=True, blank=True)
    rating = models.DecimalField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
        max_digits=3, decimal_places=2, default=2.50)
    num_ratings = models.IntegerField(default=0)
    user_rated = models.TextField(default='')
    reagents = models.TextField(default='')
    protocol_steps = models.TextField(default='')

    def details(self):
        return self.author + ', ' + self.title + ', ' + self.description








