from django.contrib import admin
from business.models import AdminHOD, Profile,Staffs,Courses,Subjects,Students,Attendance,AttendanceReport\
    ,LeaveReportStudent,LeaveReportStaff,FeedBackStudent,FeedBackStaffs

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from django.contrib.auth import get_user_model 
User = get_user_model()


# class UserModel(UserAdmin):
#     pass
admin.site.register(Profile)#,UserModel)
# admin.site.register(User, UserAdmin)




admin.site.register(AdminHOD)
admin.site.register(Staffs)
admin.site.register(Courses)
admin.site.register(Subjects)
admin.site.register(Students)
admin.site.register(Attendance)
admin.site.register(AttendanceReport)
admin.site.register(LeaveReportStudent)
admin.site.register(LeaveReportStaff)
admin.site.register(FeedBackStudent)
admin.site.register(FeedBackStaffs)

