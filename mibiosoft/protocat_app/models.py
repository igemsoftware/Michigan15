from django.db import models

# Create your models here.

# example snippet:
class Protocol(models.Model):
    title = models.TextField()
    author = models.TextField()
    date_of_upload = models.DateField
