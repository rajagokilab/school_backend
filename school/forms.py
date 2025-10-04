from django import forms
from .models import Student, Teacher, Course, Exam, Attendance, Marks
from django.contrib.auth.models import User

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['user', 'roll_number', 'grade', 'parents_email']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['user', 'subject']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'teacher']

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['name', 'course', 'date']

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'date', 'status']

class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = ['student', 'exam', 'marks']
from django import forms
from django.contrib.auth.models import User
from .models import Teacher

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['user', 'subject']
