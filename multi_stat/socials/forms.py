from django import forms
from django.contrib.auth.models import User
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.ModelForm):
    password = forms.CharField()

    class Meta:
        model = Profile
        fields = ("username", "phone", "email")


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("username", "phone", "email", "avatar")
