from django.db import models

# Create your models here.

class Usuario(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=55)
    active = models.BooleanField(default=False)

    token = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.username
