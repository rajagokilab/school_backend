from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Teacher, Course, Exam, Marks, Attendance
from .forms import StudentForm, TeacherForm, CourseForm, ExamForm, MarksForm, AttendanceForm
from django.contrib.auth.decorators import login_required

# Home
def home(request):
    return render(request, 'school/home.html')

# Students
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

# Courses
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

# Exams
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

# Attendance
def attendance_list(request):
    attendance_list = Attendance.objects.all()
    return render(request, 'school/attendance_list.html', {'attendance_list': attendance_list})

def add_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm()
    return render(request, 'school/form.html', {'form': form, 'title': 'Add Attendance'})

# Marks
def marks_list(request):
    marks_list = Marks.objects.all()
    return render(request, 'school/marks_list.html', {'marks_list': marks_list})

def add_marks(request):
    if request.method == 'POST':
        form = MarksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('marks_list')
    else:
        form = MarksForm()
    return render(request, 'school/form.html', {'form': form, 'title': 'Add Marks'})

# Parent Dashboard
# @login_required
# def parent_dashboard(request):
#     try:
#         student = Student.objects.get(parent_user=request.user)
#         attendance = Attendance.objects.filter(student=student)
#         marks = Marks.objects.filter(student=student)
#         return render(request, 'school/parent_dashboard.html', {
#             'student': student,
#             'attendance': attendance,
#             'marks': marks
#         })
#     except Student.DoesNotExist:
#         return render(request, 'school/parent_dashboard.html', {'error': 'No student linked to your account.'})
# views.py

from django.shortcuts import render, redirect
from .models import Teacher
from .forms import TeacherForm

# List all teachers
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'school/teacher_list.html', {'teachers': teachers})

# Add a new teacher
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
from django.contrib.auth.decorators import login_required
from .models import Student, Marks, Attendance

@login_required
def parent_dashboard(request):
    parent = request.user
    students = Student.objects.filter(parent_user=parent)

    if not students.exists():
        return render(request, 'school/parent_dashboard.html', {'message': 'No student linked to your account.'})

    # Get marks and attendance for all children
    marks = Marks.objects.filter(student__in=students).select_related('exam', 'subject', 'student')
    attendance = Attendance.objects.filter(student__in=students).select_related('student', 'course')

    return render(request, 'school/parent_dashboard.html', {
        'students': students,
        'marks': marks,
        'attendance': attendance
    })
