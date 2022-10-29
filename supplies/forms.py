from django import forms

class ProductForm(forms.Form):
    form_tittle = forms.CharField(label="Title")
    form_price = forms.CharField(label="Price", widget=forms.Textarea)
    form_contact = forms.CharField(label="Contact")
