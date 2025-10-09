from django.contrib import admin
from .models import Student, Teacher, Course, Exam, Marks, Attendance

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Exam)
admin.site.register(Marks)
admin.site.register(Attendance)
