from django import forms
from .models import FAQ

# class Form(forms.ModelForm):
#     class Meta:
#         model = FAQ
#         fields = ['question']

#         labels = {'question':''}

#         widgets = {
#             'question' : forms.TextInput(attrs=
#             {
#              'class':'form-control',
#              'placeholder':'Drop your question',
#              'id':'que_id'   
#             })
#         }

class Form(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = [
                'question',
                ]
