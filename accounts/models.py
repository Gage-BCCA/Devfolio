from django.db import models

# Create your models here.

class Account(models.Model):
    ACCOUNT_TYPE = (
        ('employee', 'Employee'),
        ('employer', "Employer"),
    )

    name = models.CharField(max_length=50)
    account_type = models.CharField(choices=ACCOUNT_TYPE, max_length=10)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)

    def __str__(self):
        return self.name