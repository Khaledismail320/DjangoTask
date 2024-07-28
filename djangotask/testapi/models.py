from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    gender = models.CharField(max_length=60)
    password = models.CharField(max_length=60)


