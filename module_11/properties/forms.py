from django import forms
from .models import Property, PropertyImage

class PropertyForm(forms.ModelForm):
    image = forms.ImageField(
        required=False,
        label="Cover Image",
        widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'})
    )

    class Meta:
        model = Property
        fields = [
            "title",
            "description",
            "property_type",
            "location",
            "monthly_rent",
            "bedrooms",
            "bathroom",
            "availability_status",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-input", "placeholder": "e.g. Modern Penthouse with City View"}),
            "description": forms.Textarea(attrs={"class": "form-input", "rows": 4, "placeholder": "Describe the key features, amenities, and details..."}),
            "property_type": forms.Select(attrs={"class": "form-select"}),
            "location": forms.TextInput(attrs={"class": "form-input", "placeholder": "e.g. Downtown Berlin, Mitte"}),
            "monthly_rent": forms.NumberInput(attrs={"class": "form-input", "step": "0.01", "min": "0", "placeholder": "1200.00"}),
            "bedrooms": forms.NumberInput(attrs={"class": "form-input", "min": "1"}),
            "bathroom": forms.NumberInput(attrs={"class": "form-input", "min": "1"}),
            "availability_status": forms.CheckboxInput(attrs={"class": "form-checkbox"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["property_type"].empty_label = "Select property type"
        self.fields["availability_status"].label = "Currently Available for Rent"

    def save(self, commit=True, owner=None):
        instance = super().save(commit=False)
        if owner and not instance.pk:
            instance.owner = owner
        if commit:
            instance.save()
            image_file = self.cleaned_data.get("image")
            if image_file:
                PropertyImage.objects.create(property=instance, image=image_file)
        return instance


class PropertyImageForm(forms.ModelForm):
    class Meta:
        model = PropertyImage
        fields = ["image"]