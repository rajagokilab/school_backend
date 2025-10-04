from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Teacher, Course, Exam, Attendance, Marks
from .forms import StudentForm, TeacherForm, CourseForm, ExamForm, AttendanceForm, MarksForm
from django.contrib.auth.decorators import login_required

# Home Page
def home(request):
    return render(request, 'school/home.html')

# --- CRUD Views ---
def student_list(request):
    students = Student.objects.all()
    return render(request, 'school/student_list.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'school/form.html', {'form': form, 'title': 'Add Student'})

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'school/teacher_list.html', {'teachers': teachers})

def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm()
    return render(request, 'school/form.html', {'form': form, 'title': 'Add Teacher'})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'school/course_list.html', {'courses': courses})

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'school/form.html', {'form': form, 'title': 'Add Course'})

def exam_list(request):
    exams = Exam.objects.all()
    return render(request, 'school/exam_list.html', {'exams': exams})

def add_exam(request):
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exam_list')
    else:
        form = ExamForm()
    return render(request, 'school/form.html', {'form': form, 'title': 'Add Exam'})

def attendance_list(request):
    attendance = Attendance.objects.all()
    return render(request, 'school/attendance_list.html', {'attendance': attendance})

def add_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm()
    return render(request, 'school/form.html', {'form': form, 'title': 'Add Attendance'})

def marks_list(request):
    marks = Marks.objects.all()
    return render(request, 'school/marks_list.html', {'marks': marks})

def add_marks(request):
    if request.method == 'POST':
        form = MarksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('marks_list')
    else:
        form = MarksForm()
    return render(request, 'school/form.html', {'form': form, 'title': 'Add Marks'})

# --- Parent Dashboard ---
@login_required
def parent_dashboard(request):
    try:
        student = Student.objects.get(parents_email=request.user.email)
        attendance = Attendance.objects.filter(student=student)
        marks = Marks.objects.filter(student=student)
        return render(request, 'school/parent_dashboard.html', {
            'student': student,
            'attendance': attendance,
            'marks': marks
        })
    except Student.DoesNotExist:
        return render(request, 'school/parent_dashboard.html', {'error': 'No student linked to your account.'})
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'school/course_list.html', {'courses': courses})
from django.shortcuts import render, redirect
from .forms import CourseForm
from .models import Course

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'school/form.html', {'form': form, 'title': 'Add Course'})
from django.shortcuts import render, redirect
from .forms import TeacherForm
from .models import Teacher

def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm()
    return render(request, 'school/form.html', {'form': form, 'title': 'Add Teacher'})
from django.shortcuts import render
from .models import Exam

def exam_list(request):
    exams = Exam.objects.all()
    return render(request, 'school/exam_list.html', {'exams': exams})
from django.shortcuts import render
from .models import Attendance

def attendance_list(request):
    attendance_list = Attendance.objects.all()
    return render(request, 'school/attendance_list.html', {'attendance_list': attendance_list})
from django.shortcuts import render
from .models import Marks

def marks_list(request):
    marks_list = Marks.objects.all()
    return render(request, 'school/marks_list.html', {'marks_list': marks_list})
# views.py
from django.shortcuts import render
from .models import Student, Attendance, Marks

def parent_dashboard(request):
    # Assuming parent is logged in
    try:
        student = Student.objects.get(parent_user=request.user)
        attendance = Attendance.objects.filter(student=student)
        marks = Marks.objects.filter(student=student)
    except Student.DoesNotExist:
        student = None
        attendance = []
        marks = []

    return render(request, 'school/parent_dashboard.html', {
        'student': student,
        'attendance': attendance,
        'marks': marks
    })
