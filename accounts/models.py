from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
    ACCOUNT_TYPE = (
        ('employee', 'Employee'),
        ('employer', "Employer"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_type = models.CharField(choices=ACCOUNT_TYPE, max_length=10)

    def __str__(self):
        return self.user.username