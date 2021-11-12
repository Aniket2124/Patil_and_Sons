from django.shortcuts import render,HttpResponseRedirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def home(request):
    return render(request,'business/home.html')


def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Account Created Successfully..!')
    else:
        fm = SignUpForm()
    return render(request, 'business/signup.html', {'form':fm})


#Login 
def user_login(request):
    if not request.user is authenticate():
        if request.method=="POST":
            fm = AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    return render(request,'business/profile.html')
        else:
            fm = AuthenticationForm()
        return render(request,'business/login.html',{'form': fm})
    else:
        return HttpResponseRedirect('business/home.html')

#Profile
def user_profile(request):
    if not request.user is authenticate():
        return render(request,'business/profile.html')
    else:
        return HttpResponseRedirect('business/home.html')



#logout

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('business/home.html')



    
 