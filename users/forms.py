from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import AdtaaUser


class AdtaaUserForm(UserCreationForm):
    class Meta:
        model = AdtaaUser
        fields = [
            'email', 'username', 'password1', 'password2', 'accessRequested'
        ]
