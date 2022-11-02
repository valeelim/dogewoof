from django import forms
from .models import DogItem

class DogItemForm(forms.Form):
    item_title = forms.CharField(max_length=32)
    price = forms.IntegerField()
    breed = forms.CharField(max_length=16)
    description = forms.CharField(max_length=256)
    image = forms.ImageField()
    contact = forms.CharField(max_length=32)

class DogItemFormModel(forms.ModelForm):
    class Meta:
        model = DogItem
        exclude = ['user']
        fields = "__all__"