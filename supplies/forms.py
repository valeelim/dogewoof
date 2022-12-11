from django import forms
from .models import Product


class ProductForm(forms.Form):
    title = forms.CharField(max_length=250)
    price = forms.CharField(max_length=250)
    description = forms.CharField(max_length=250)
    contact = forms.CharField(max_length=280)

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

    def save(self):
        Product(title=self.cleaned_data['title'], price=self.cleaned_data['price'], description=self.cleaned_data['description'], contact=self.cleaned_data['contact']).save()

