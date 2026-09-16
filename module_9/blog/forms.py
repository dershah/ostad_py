from django import forms
from django.forms import ModelForm
from .models import Blog

class BlogForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':'Enter Blog Title',
            'class':'input-box'
        }
    ))
    content = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':'Enter Blog Title',
            'class':'input-box'
        }
    ))

    class Meta:
        model = Blog
        fields = ['title','content']