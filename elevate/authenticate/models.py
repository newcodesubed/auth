from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)
