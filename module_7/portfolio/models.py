from django.db import models

# Create your models here.
class project(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    technology_used = models.CharField(max_length=50)
    git_link= models.CharField(max_length=100)