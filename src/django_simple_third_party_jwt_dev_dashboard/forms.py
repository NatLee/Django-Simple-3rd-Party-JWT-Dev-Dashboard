from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username",)


class UserForm(forms.ModelForm):
  password = forms.CharField(label='Password', widget=forms.PasswordInput)
  username = forms.CharField(label='Username')

  class Meta:
    model = User
    fields =['username','password']