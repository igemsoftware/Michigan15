from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import ModelForm

class UserRegistration(models.Model):
    email = models.EmailField(blank=False)
    user_name = models.CharField(max_length=50, default='YourName', blank=False)
    password = models.CharField(max_length=120, default='password123', blank=False)

    def __str__(self):
        return (self.user_name + ', ' + self.email)

class UserAuthentication(models.Model):
    user_name = models.CharField(max_length=50, default='YourUserName')
    password = models.CharField(max_length=120, default='password123', blank=False)

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
