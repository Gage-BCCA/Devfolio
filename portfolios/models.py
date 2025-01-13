from django.db import models
from accounts.models import Account

class Portfolio(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    projects = models.TextField(blank=True, null=True)
    social_links = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.account.name}'s Portfolio" # String representation of the Portfolio object
    
