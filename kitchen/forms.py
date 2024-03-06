from django import forms
from .models import FoodMenu


class MenuForm(forms.ModelForm):
    name = forms.CharField(label="",widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "enter name"}))
    price = forms.CharField(label="",
                               widget=forms.TextInput(attrs={"class": "form-control", "placeholder": " price"}))

    class Meta:
        model = FoodMenu
        fields = ['name', 'price', 'image']


class UpdateMenuForm(forms.ModelForm):
    name = forms.CharField(label="",
                           widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "enter name"}))
    price = forms.CharField(label="",
                            widget=forms.TextInput(attrs={"class": "form-control", "placeholder": " price"}))

    class Meta:
        model = FoodMenu
        fields = ['name', 'price', 'image']






