from django import forms
from . import models
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='password repeat', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("password and password2 aren't equal")
        return cd['password2']


class ShortForm(forms.ModelForm):
    class Meta:
        model = models.Shorts
        fields = ('fullurl',)
