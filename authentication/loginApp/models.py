from django.db import models

# Create your models here.

class Usuarios(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    