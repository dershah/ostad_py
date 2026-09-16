from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class user_registration_form(UserCreationForm):
    first_name =forms.CharField(widget=forms.TextInput(
        attrs = {
            'placeholder' : 'Enter your First Name',
            'class' : 'input-box'
        }))
    last_name =forms.CharField(widget=forms.TextInput(
        attrs = {
            'placeholder' : 'Enter your Last Name',
            'class' : 'input-box'
        }))
    email =forms.CharField(widget=forms.EmailInput(
        attrs = {
            'placeholder' : 'Enter your Email',
            'class' : 'input-box'
        }))
    password1 =forms.CharField(widget=forms.PasswordInput(
        attrs = {
            'placeholder' : 'Enter New Password',
            'class' : 'input-box'
        }))
    password2 =forms.CharField(widget=forms.PasswordInput(
        attrs = {
            'placeholder' : 'Confirm Password',
            'class' : 'input-box'
        }))

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

class user_authentication_form(AuthenticationForm):
    username = forms.CharField(widget=forms.EmailInput(
        attrs = {
            'placeholder' : 'Enter your Email',
            'class' : 'input-box'
        }))
    password =forms.CharField(widget=forms.PasswordInput(
        attrs = {
            'placeholder' : 'Enter New Password',
            'class' : 'input-box'
        }))