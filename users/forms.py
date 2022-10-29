from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'required': '',
            'name': 'username',
            'id': 'username',
            'type': 'text',
            'placeholder': 'Uncle Roger',
            'class': 'form-control',
            'value': '',
        })
        self.fields['email'].widget.attrs.update({
            'required': '',
            'name': 'email',
            'id': 'email',
            'type': 'email',
            'placeholder': 'uncle@roger.com',
            'class': 'form-control',
        })

    class Meta:
        model = User
        fields = ('username', 'email',)

    def clean(self):
        super(UserUpdateForm, self).clean()
        username = self.cleaned_data.get('username')
        
        if len(username) < 4:
            self._errors['username'] = self.error_class(['Username must be at least 4 characters'])

        return self.cleaned_data


class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['image']