from django import forms
from .models import RentalRequest, Review, RequestStatus

class RentalRequestForm(forms.ModelForm):
    class Meta:
        model = RentalRequest
        fields = ["message"]
        widgets = {
            "message": forms.Textarea(attrs={
                "class": "form-input",
                "rows": 3,
                "placeholder": "Introduce yourself to the owner and express your interest...",
            }),
        }

    def __init__(self, *args, **kwargs):
        self.property_obj = kwargs.pop("property_obj", None)
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        if self.property_obj and self.user:
            if self.property_obj.owner == self.user:
                raise forms.ValidationError("You cannot send a rental request for your own property.")
            
            pending_exists = RentalRequest.objects.filter(
                property=self.property_obj,
                tenant=self.user,
                status=RequestStatus.PENDING
            ).exists()
            
            if pending_exists:
                raise forms.ValidationError("You already have a pending rental request for this property.")
        return cleaned_data


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["rating", "comment"]
        widgets = {
            "rating": forms.Select(
                choices=[(1, "1 Star ★"), (2, "2 Stars ★★"), (3, "3 Stars ★★★"), (4, "4 Stars ★★★★"), (5, "5 Stars ★★★★★")],
                attrs={"class": "form-select"}
            ),
            "comment": forms.Textarea(attrs={
                "class": "form-input",
                "rows": 3,
                "placeholder": "Share your experience staying or communicating regarding this property...",
            }),
        }

    def __init__(self, *args, **kwargs):
        self.property_obj = kwargs.pop("property_obj", None)
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        if self.property_obj and self.user:
            accepted = RentalRequest.objects.filter(
                property=self.property_obj,
                tenant=self.user,
                status=RequestStatus.ACCEPTED
            ).exists()
            if not accepted:
                raise forms.ValidationError("You can only leave a review if your rental request was accepted.")

            already_reviewed = Review.objects.filter(
                property=self.property_obj,
                tenant=self.user
            ).exists()
            if already_reviewed:
                raise forms.ValidationError("You have already submitted a review for this property.")
        return cleaned_data
