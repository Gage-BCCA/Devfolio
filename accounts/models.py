from django.db import models

# Create your models here.

class Account(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=50)
    links = models.CharField(max_length=200)
    password = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)

    def __str__(self):
        return self.name