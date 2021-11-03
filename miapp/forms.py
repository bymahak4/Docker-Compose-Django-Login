from django import forms
from django.core import validators
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.contrib.auth.models import User


class registerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']

class PasswordResetRequestForm(forms.Form):
    email = forms.CharField(label=("Email"), max_length=254)

