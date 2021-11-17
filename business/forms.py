from django import forms
from django.contrib.auth import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db.models.base import Model
from django.forms import fields
from .models import Courses,Subjects,Students,Staffs,AdminHOD,Profile#CustomUser
from django.contrib.auth import get_user_model
from django_countries.widgets import CountrySelectWidget
User = get_user_model()



class SignUpForm(UserCreationForm):
    # choice = forms.CharField(label='Choice',widget=forms.ChoiceField(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta(UserCreationForm.Meta):
        model = Profile
        fields = ['username','first_name','last_name','email','contact_number', 'location']
        labels = {'email':'Email'}

        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'contact_number': forms.NumberInput(attrs={'placeholder': 'Enter contact number', 'class': 'form-control'}),
            'location': CountrySelectWidget(attrs={'class': 'form-control'}, layout='{widget}'),
         
        }

class UserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = Profile
        fields = ['username','first_name','last_name','email','date_joined']
        labels = {'email':'Email'}
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'date_joined': forms.DateTimeInput(attrs={'class':'form-control'}),
        }


class AdminProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = Profile
        fields = ['username','first_name','last_name','email','date_joined']
        labels = {'email':'Email'}
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'date_joined': forms.DateTimeInput(attrs={'class':'form-control'}),
        }



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





