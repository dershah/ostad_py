from django import forms
from django.forms import ModelForm
from .models import Item

class ItemEntryForm(ModelForm):
    name= forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':'Enter Item Name',
            'class':'input_box'
        }))
    type = forms.ChoiceField(choices=Item.ItemType.choices, 
        widget=forms.Select(
        attrs={'class': 'input_box'
        }))   
    category= forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':'Enter The Category',
            'class':'input_box'
        }))
    description= forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':'Enter A Short Description',
            'class':'input_box'
        }))
    location= forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':'Enter Location',
            'class':'input_box'
        }))
    contact= forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':'Enter Contact Number',
            'class':'input_box'
        }))
    # status =forms.ChoiceField(choices=Item.ItemStatus.choices,
    #         widget=forms.Select(
    #         attrs={'class': 'input_box'
    #     }))
    
    class Meta:
        model = Item
        fields = ['name', 'type', 'category', 'description', 'location', 'contact']



class ItemStatusForm(ModelForm):
    status = forms.ChoiceField(
        choices=Item.ItemStatus.choices,
        widget=forms.Select(attrs={'class': 'input_box'})
    )

    class Meta:
        model = Item
        fields = ['status']  