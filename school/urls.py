from django.urls import path
from . import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('parent-login/', LoginView.as_view(template_name='school/parent_login.html'), name='parent_login'),
    path('parent-dashboard/', views.parent_dashboard, name='parent_dashboard'),    path('', views.home, name='home'),
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.add_student, name='add_student'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/add/', views.add_teacher, name='add_teacher'),
    path('courses/', views.course_list, name='course_list'),
    path('courses/add/', views.add_course, name='add_course'),
    path('exams/', views.exam_list, name='exam_list'),
    path('exams/add/', views.add_exam, name='add_exam'),
    path('attendance/', views.attendance_list, name='attendance_list'),
    path('attendance/add/', views.add_attendance, name='add_attendance'),
    path('marks/', views.marks_list, name='marks_list'),
    path('marks/add/', views.add_marks, name='add_marks'),
]
