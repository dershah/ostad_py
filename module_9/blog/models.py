from django.db import models
from users.models import CustomUser

class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=250)
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='items'
    )  

    def __str__(self):
        return self.title