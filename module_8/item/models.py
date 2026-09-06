from django.db import models
from user.models import CustomUser


class Item(models.Model):
    class ItemType(models.TextChoices):
        LOST = 'Lost'
        FOUND = 'Found'
    class ItemStatus(models.TextChoices):
        ACTIVE = 'Active'
        RESOLVED = 'resolved'

    name = models.CharField(max_length=50)
    type = models.CharField(max_length=5, choices=ItemType.choices)
    category = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    location = models.CharField(max_length=128)
    contact = models.CharField(max_length=15)
    status = models.CharField(max_length=8, choices=ItemStatus.choices)

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='items'
    )   