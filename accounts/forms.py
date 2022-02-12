from django import forms
from .models import Account, UserProfile
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from django.core.mail import send_mail


class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class': 'form-control',
    }))

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password'
    }))

    class Meta:
        model = Account
        fields = ('first_name', 'last_name',
                  'phone_number', 'email', 'password')

    def clean(self):
        cleaned_data = super(SignupForm, self).clean()
        password = self.cleaned_data['password']
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")


class UserForm(forms.ModelForm):
    pass


class UserProfileForm(forms.ModelForm):
    pass
