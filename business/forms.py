from django import forms
from django.contrib.auth import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db.models.base import Model
from django.forms import fields
from .models import Courses,Subjects,Students,Staffs,AdminHOD


class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'email':'Email'}

class UserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','date_joined']
        labels = {'email':'Email'}

class AdminProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','date_joined']
        labels = {'email':'Email'}


class Course(forms.ModelForm):
    class Meta:
        model = Courses
        fields = '__all__'
    
class Subject(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = '__all__'

class Student(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    class Meta:
        model = Students
        fields = '__all__'

class Staff(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    class Meta:
        model = Staffs
        fields = '__all__'


class HOD(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    class Meta:
        model = AdminHOD
        fields = '__all__'


