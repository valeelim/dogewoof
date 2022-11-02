from django.contrib.auth.models import User
from django.forms import ModelForm
from.models import UserProfile

class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['picture', 'bio', 'phone', 'address', 'dogtype']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['picture'].required = False
        self.fields['bio'].required = False
        self.fields['phone'].required = False
        self.fields['address'].required = False
        self.fields['dogtype'].required = False

class SaldoForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['saldo']
