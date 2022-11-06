from django import forms
from .models import Product


class ProductForm(forms.Form):
    class Meta:
        model = Product
        field = ('title', 'image', 'price', 'description', 'contact',)
