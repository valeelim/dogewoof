from django import forms

class DonationForm(forms.Form):
    amount = forms.IntegerField(label='', max_value=999999999)

    def __init__(self, *args, **kwargs):
        super(DonationForm, self).__init__(*args, **kwargs)
        self.fields['amount'].widget.attrs.update({
            'placeholder': 'Enter Donation Amount',
        })

