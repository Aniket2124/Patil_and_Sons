from django.contrib.auth.models import AbstractUser,User
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    is_admin = models.BooleanField('Is admin',default=False)
    # is_active = models.BooleanField('Is active',default=False)
    is_staff = models.BooleanField('Is staff',default=False)
    is_student = models.BooleanField('Is student',default=False)

    # email = models.EmailField(
    #     verbose_name='email address',
    #     max_length=255,
    #     unique=True,
    # )
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []

    # # objects = MyUserManager()

    # def __str__(self):
    #     return self.email



#     user_type_data=((1,"HOD"),(2,"Staff"),(3,"Student"))
#     user_type=models.CharField(default=1,choices=user_type_data,max_length=10)

class AdminHOD(models.Model):
    # id=models.AutoField(primary_key=True)
    # name=models.CharField(max_length=255)
    # email=models.EmailField(max_length=255)  
    # password=models.CharField(max_length=255)    
    admin_record = models.ForeignKey(CustomUser,on_delete=models.SET_NULL, null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()


    def __str__(self):
        return self.name

class Staffs(models.Model):
    # id=models.AutoField(primary_key=True)
    # name=models.CharField(max_length=255)
    # email=models.EmailField(max_length=255)  
    # password=models.CharField(max_length=255) 
    staff_record = models.ForeignKey(CustomUser,on_delete=models.SET_NULL, null=True, blank=True)
    address=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()
    def __str__(self):
        return self.name

class Courses(models.Model):
    id=models.AutoField(primary_key=True)
    course_name=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()
    
    def __str__(self):
        return self.course_name

class Subjects(models.Model):
    id=models.AutoField(primary_key=True)
    subject_name=models.CharField(max_length=255)
    course_id=models.ForeignKey(Courses,on_delete=models.SET_NULL, null=True, blank=True,default=1)    
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

    def __str__(self):
        return self.subject_name

class Students(models.Model):
    # id=models.AutoField(primary_key=True)
    # name=models.CharField(max_length=255)
    # email=models.EmailField(max_length=255)  
    # password=models.CharField(max_length=255)  
    stud_record = models.ForeignKey(CustomUser,on_delete=models.SET_NULL, null=True, blank=True)
    gender=models.CharField(max_length=255)
    profile_pic=models.ImageField(upload_to='profile')
    address=models.TextField()
    course_id=models.ForeignKey(Courses,on_delete=models.SET_NULL, null=True, blank=True)
    session_start_year=models.DateField()
    session_end_year=models.DateField()
    # created_at=models.DateTimeField(auto_now_add=True)
    # updated_at=models.DateTimeField(auto_now_add=True)
    # objects = models.Manager()
    token =models.PositiveIntegerField()

    def __str__(self):
        return self.stud_record.username


class Attendance(models.Model):
    id=models.AutoField(primary_key=True)
    subject_id=models.ForeignKey(Subjects,on_delete=models.SET_NULL, null=True, blank=True)
    attendance_date=models.DateTimeField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class AttendanceReport(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Students,on_delete=models.SET_NULL, null=True, blank=True)
    attendance_id=models.ForeignKey(Attendance,on_delete=models.SET_NULL, null=True, blank=True)
    status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class LeaveReportStudent(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Students,on_delete=models.SET_NULL, null=True, blank=True)
    leave_date=models.CharField(max_length=255)
    leave_message=models.TextField()
    leave_status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class LeaveReportStaff(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staffs, on_delete=models.SET_NULL, null=True, blank=True)
    leave_date = models.CharField(max_length=255)
    leave_message = models.TextField()
    leave_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class FeedBackStudent(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.SET_NULL, null=True, blank=True)
    feedback = models.TextField()
    feedback_reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class FeedBackStaffs(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staffs, on_delete=models.SET_NULL, null=True, blank=True)
    feedback = models.TextField()
    feedback_reply=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()