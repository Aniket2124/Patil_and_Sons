from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponseRedirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm,UserProfileForm,AdminProfileForm,Course,Subject,Student,Staff,HOD
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.db import models
from business.models import *

# Create your views here.

def home(request):
    return render(request,'business/home.html',{'name':request.user})


def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Account Created Successfully..!')
            return HttpResponseRedirect('/login/')
    else:
        fm = SignUpForm()
    return render(request, 'business/signup.html', {'form':fm})


#Login 
def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            fm = AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/')
        else:
            fm = AuthenticationForm()
        return render(request,'business/login.html',{'form': fm})
    else:
        messages.success(request, 'Login successfully...!')
        return HttpResponseRedirect('/')

#Profile
def user_profile(request):
    if request.user.is_authenticated:
        fm = UserProfileForm(instance=request.user)
        return render(request,'business/profile.html',{'name':request.user,'form':fm})
    else:
        return HttpResponseRedirect('/login/')

#Edit Profile
def user_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.user.is_superuser == True:
                fm = AdminProfileForm(request.POST,instance=request.user)
            else:    
                fm = UserProfileForm(request.POST,instance=request.user)
            if fm.is_valid():
                messages.success(request, 'Profile Updated successfully...!')
                fm.save()
                
        else:
            if request.user.is_superuser == True:
                fm = AdminProfileForm(instance=request.user)
            else:
                fm = UserProfileForm(instance=request.user)
        return render(request,'business/profile.html',{'name':request.user.username,'form':fm})
    else:
        return HttpResponseRedirect('/login/')


#logout

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

#Change Password with old password
def user_change_pass1(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = SetPasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request, 'Password Changed successfully...!')
                return HttpResponseRedirect('/profile/')
        else:
            fm = SetPasswordForm(user=request.user)
        return render(request,'business/change_pass1.html',{'name':request.user,'form':fm})
    else:
        return HttpResponseRedirect('/login/')

#change Password 
def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request, 'Password Changed successfully...!')
                return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request,'business/change_pass.html',{'name':request.user,'form':fm})
    else:
        return HttpResponseRedirect('/login/')



#-------------------------------------------------------------------------------------------------------------------------------#
# Course
def course(request):
    if request.method == "POST":
        fm = Course(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Data Saved Successfully..!')
            return HttpResponseRedirect('/')
    else:  
        fm = Course()      
        return render(request,'business/course.html',{'form':fm})


def course_details(request):
    cor = Courses.objects.all()
    return render(request,'business/course_details.html',{'course':cor})

def course_delete(request,id):
    # if request.method == "POST":
    cor = Courses.objects.get(pk=id)
    cor.delete()
    messages.success(request,'Course Deleted Successfully..!')
    return HttpResponseRedirect('/',{'course':cor})
    # return render(request,'business/course_details.html',{'course':cor})





#-------------------------------------------------------------------------------------------------------------------------------#
# Subject
def subject(request):
    if request.method == "POST":
        fm = Subject(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Data Saved Successfully..!')
            return HttpResponseRedirect('/')
    else:  
        fm = Subject()      
        return render(request,'business/course.html',{'form':fm})




#-------------------------------------------------------------------------------------------------------------------------------#
# Student
def student(request):
    if request.method == "POST":
        fm = Student(request.POST,request.FILES)
       
        if fm.is_valid():
            fm.save()
            messages.success(request,'Data Saved Successfully..!')
            return HttpResponseRedirect('/')       
    else:  
        fm = Student()
    return render(request,'business/student.html',{'form':fm})




#------------------------------------------------------------------------------------------------------------------------------#
#Staff
def staff(request):
    if request.method == "POST":
        fm = Staff(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Data Saved Successfully..!')
            return HttpResponseRedirect('/')
    else:  
        fm = Staff()      
    return render(request,'business/add_staff.html',{'form':fm})




#--------------------------------------------------------------------------------------------------------------------------------#
#AdminHOD
def admin_hod(request):
    if request.method == "POST":
        fm = HOD(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Data Saved Successfully..!')
            return HttpResponseRedirect('/')
    else:  
        fm = HOD()      
    return render(request,'business/admin_hod.html',{'form':fm})













    
 