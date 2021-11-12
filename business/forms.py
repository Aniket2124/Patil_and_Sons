from django import forms
from django.contrib.auth import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.db.models.base import Model
from django.forms import fields


class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'email':'Email'}

# class UserLoginForm(AuthenticationForm):
#     class Meta:
#         model = User
#         fields = ['username','password']



