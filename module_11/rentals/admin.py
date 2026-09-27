from django.contrib import admin
from .models import RentalRequest, Review


@admin.register(RentalRequest)
class RentalRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'property', 'tenant', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at')
    search_fields = ('property__title', 'tenant__email', 'message')
    list_editable = ('status',)
    raw_id_fields = ('property', 'tenant')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'property', 'tenant', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('property__title', 'tenant__email', 'comment')
    raw_id_fields = ('property', 'tenant')
