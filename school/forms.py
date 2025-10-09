from django import forms
from .models import Student, Teacher, Course, Exam, Attendance, Marks

# --- Student Form ---
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['user', 'enrollment_number', 'grade', 'parent_user', 'courses']

# --- Teacher Form ---
class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['user', 'employee_id', 'courses']

# --- Course Form ---
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'code', 'teacher']

# --- Exam Form ---
class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['course', 'date', 'total_marks']

# --- Attendance Form ---
class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'course', 'date', 'status']

# --- Marks Form ---
class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = ['student', 'subject', 'exam', 'marks']  # ✅ Correct fields
