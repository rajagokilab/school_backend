from django.contrib import admin
from .models import Teacher, Student, Course, Exam, Attendance, Marks

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Exam)
admin.site.register(Attendance)
admin.site.register(Marks)
