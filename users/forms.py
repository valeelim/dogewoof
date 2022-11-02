from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio', 'phone']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False
        self.fields['bio'].required = False
        self.fields['phone'].required = False

class TopUpForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['saldo']