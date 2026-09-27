from django.db import models
from accounts.models import CustomUser
from common.models import TimeStampMixin

class PropertyType(models.TextChoices):
    APARTMENT = "APARTMENT", "Apartment"
    HOUSE = "HOUSE", "House"
    ROOM = "ROOM", "Room"
    OFFICE = "OFFICE", "Office"


class Property(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete= models.CASCADE, related_name='properties')
    title = models.CharField(max_length=200)
    description = models.CharField()
    property_type = models.CharField(max_length=20, choices=PropertyType.choices, db_index =True)
    location = models.CharField(max_length=255, db_index=True)
    monthly_rent = models.DecimalField(max_digits=10,decimal_places=2)
    bedrooms = models.PositiveSmallIntegerField(default=1)
    bathroom = models.PositiveSmallIntegerField(default=1)
    availability_status = models.BooleanField(default=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'
        ordering = ("-created_at",)
        indexes = [
            models.Index(fields=["location", "property_type"]),
            models.Index(fields=["-created_at"]),
        ]
        permissions = [("can_publish_property", "Can publish property")]

    def __str__(self):
        return f"{self.title} — {self.location}"


class PropertyImage(TimeStampMixin):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')

    class Meta:
        verbose_name = 'Property Image'
        verbose_name_plural = 'Property Images'

    def __str__(self):
        return f"Image for {self.property.title}"

