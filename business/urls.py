from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('signup/',views.sign_up, name='signup'),
    path('login/',views.user_login, name='login'),
    path('profile/',views.user_profile, name='profile'),
    path('logout/',views.user_logout, name='logout'),
    path('change_pass/',views.user_change_pass, name='change_pass'),
    path('change_pass1/',views.user_change_pass1, name='change_pass1'),
    path('course/',views.course, name='course'),
    path('subject/',views.subject, name='subject'),
    path('student/',views.student, name='student'),
]