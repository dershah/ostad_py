from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class user_registration_form(UserCreationForm):

    first_name= forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':'Enter First Name',
            'class':'input_box'
        }))
    last_name= forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':'Enter Last Name',
            'class':'input_box'
        }))
    email= forms.CharField(widget=forms.EmailInput(
        attrs={
            'placeholder':'Enter Your Email',
            'class':'input_box'
        }))
    student_id= forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':'Enter Student ID',
            'class':'input_box'
        }))
    password1= forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder':'Enter Password',
            'class':'input_box'
        }))
    password2= forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder':'Confirm Password',
            'class':'input_box'
        }))
    
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'student_id', 'password1', 'password2']

class user_authentication_form(AuthenticationForm):

    username= forms.CharField(widget=forms.EmailInput(
        attrs={
            'placeholder':'Enter Your Email',
            'class':'input_box'
        }))
    password= forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder':'Enter Password',
            'class':'input_box'
        }))

        # confirm_password = forms.CharField(
    #     widget=forms.PasswordInput,
    #     label='Confirm Password'
    # )
    # class Meta:
    #     model = user_registration
    #     fields = ['name', 'username', 'email', 'password']
    #     widgets = {
    #         'password': forms.PasswordInput(),
    #     }