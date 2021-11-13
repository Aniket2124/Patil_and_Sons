from django.contrib import admin
from business.models import AdminHOD,Staffs,Courses,Subjects,Students,Attendance,AttendanceReport\
    ,LeaveReportStudent,LeaveReportStaff,FeedBackStudent,FeedBackStaffs

# Register your models here.

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

