from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserRegistrationForm(UserCreationForm):
    # role=
    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'placeholder' : 'Enter Email Address',
            'class':'input-box'
        }
    ))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder' : 'New Password',
            'class':'input-box'
        }
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder' : 'Confirm Password',
            'class':'input-box'
        }
    ))

    class Meta:
        model = CustomUser
        fields= ['role', 'email', 'password1', 'password2']
        widgets = {
            'role': forms.Select(attrs={'class': 'input-box'}),
        }


class UserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.EmailInput(
        attrs = {
            'placeholder' : 'Enter your Email',
            'class' : 'input-box'
        }))
    password =forms.CharField(widget=forms.PasswordInput(
        attrs = {
            'placeholder' : 'Enter your Password',
            'class' : 'input-box'
        }))