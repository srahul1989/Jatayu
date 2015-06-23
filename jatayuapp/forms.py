__author__ = 'rtelgote'

from django import forms
from .models import SignUp

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        domain,extension = provider.split('.')
        if not domain == 'gmail':
            raise forms.ValidationError("Please make sure you using correct domain")
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        return full_name