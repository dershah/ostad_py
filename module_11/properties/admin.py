from django.contrib import admin
from .models import Property, PropertyImage


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'property_type', 'location', 'monthly_rent', 'availability_status', 'created_at')
    list_filter = ('property_type', 'availability_status', 'created_at')
    search_fields = ('title', 'location', 'description', 'owner__email')
    inlines = [PropertyImageInline]
    list_editable = ('availability_status',)


@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    list_display = ('property', 'image', 'created_at')
    search_fields = ('property__title',)
