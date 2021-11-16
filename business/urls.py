from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

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
    path('add_staff/',views.staff, name='add_staff'),
    path('admin_hod/',views.admin_hod, name='admin_hod'),
    path('course_details/',views.course_details, name='course_details'),
    path('course_update/<int:id>/',views.course_update, name='course_update'),
    path('course_delete/<int:id>/',views.course_delete, name='course_delete'),
    path('student_login/',views.student_login, name='student_login'),
    path('otp_verification/',views.otp, name='otp'),
   
]