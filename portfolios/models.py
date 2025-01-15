from django.db import models
from accounts.models import Account

class Portfolio(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    layout = models.IntegerField()
    color_theme = models.IntegerField()
    
    def __str__(self):
        return f"{self.account.name}'s portfolio"
    
class Project(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    blurb = models.CharField(max_length=255)
    programming_language = models.CharField(max_length=50)
    project_link = models.URLField()

    def __str__(self):
        return self.title
    
class Skill(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=100)
    experience_level = models.CharField(max_length=50)
    
    def __str__(self):
        return self.skill_name

class Bio(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    bio = models.TextField()
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name    


class Link(models.Model):
    bio = models.ForeignKey(Bio, on_delete=models.CASCADE)
    link_type = models.CharField(max_length=50)
    url = models.URLField()
    
    def __str__(self):
        return self.link_type