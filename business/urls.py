from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('signup/',views.sign_up, name='signup'),
    path('login/',views.user_login, name='login'),
    path('profile/',views.user_profile, name='profile'),
]