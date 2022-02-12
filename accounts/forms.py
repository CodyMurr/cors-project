from django import forms
from .models import Account, UserProfile
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.conf import settings
from django.template.loader import render_to_string
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

    def save(self, request):

        user = super(forms.ModelForm, self).save(commit=False)
        user.is_active = False
        user.save()

        context = {
            # 'from_email': settings.DEFAULT_FROM_EMAIL,
            'request': request,
            'protocol': request.scheme,
            'username': self.cleaned_data.get('username'),
            'domain': request.META['HTTP_HOST'],
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
        }

        subject = render_to_string(
            'djangobin/email/activation_subject.txt', context)
        email = render_to_string(
            'djangobin/email/activation_email.txt', context)

        send_mail(subject, email, settings.DEFAULT_FROM_EMAIL, [user.email])

        return user


class UserForm(forms.ModelForm):
    pass


class UserProfileForm(forms.ModelForm):
    pass
