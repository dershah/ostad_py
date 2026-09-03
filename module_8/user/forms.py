from django import forms
from django.forms import ModelForm
from user.models import user_registration

class user_registration_form(ModelForm):
    confirm_password = forms.CharField(
        widget=forms.PasswordInput,
        label='Confirm Password'
    )

    class Meta:
        model = user_registration
        fields = ['name', 'username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }