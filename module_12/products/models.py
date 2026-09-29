from django.db import models
from common.models import TimeMixSetup

class Product(TimeMixSetup):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock= models.PositiveIntegerField()

    def __str__(self):
        return self.name
