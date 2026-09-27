from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from properties.models import Property
from common.models import TimeStampMixin


class RequestStatus(models.TextChoices):
    PENDING = "PENDING", "Pending"
    ACCEPTED = "ACCEPTED", "Accepted"
    REJECTED = "REJECTED", "Rejected"
    CANCELLED = "CANCELLED", "Cancelled"


class RentalRequest(TimeStampMixin):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='rental_requests')
    tenant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rental_requests')
    message = models.TextField(blank=True, default="")
    status = models.CharField(max_length=20, choices=RequestStatus.choices, default=RequestStatus.PENDING, db_index=True)

    class Meta:
        verbose_name = 'Rental Request'
        verbose_name_plural = 'Rental Requests'
        ordering = ("-created_at",)
        constraints = [
            models.UniqueConstraint(
                fields=['property', 'tenant'],
                condition=models.Q(status=RequestStatus.PENDING),
                name='unique_pending_rental_request'
            )
        ]

    def __str__(self):
        return f"Request by {self.tenant.email} for {self.property.title} ({self.get_status_display()})"


class Review(TimeStampMixin):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='reviews')
    tenant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Rating from 1 to 5 stars"
    )
    comment = models.TextField()

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        ordering = ("-created_at",)
        unique_together = ('property', 'tenant')

    def __str__(self):
        return f"{self.rating}★ Review by {self.tenant.email} for {self.property.title}"
