from django import forms

class ProductForm(forms.Form):
    task_title = forms.CharField(label="Title")
    task_price = forms.CharField(label="Price", widget=forms.Textarea)
    task_description = forms.CharField(label="Description", widget=forms.Textarea)
    task_contact = forms.CharField(label="Contact", widget=forms.Textarea)