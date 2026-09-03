from django.db import models

# Create your models here.
class user_registration(models.Model):
    user_id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField(
        max_length=254,
        error_messages={'invalid': 'Enter a valid email address.'},
        unique=True
    )
    password = models.CharField(max_length=128)