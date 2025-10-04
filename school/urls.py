from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.student_list, name='student_list'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('courses/', views.course_list, name='course_list'),
    path('courses/add/', views.add_course, name='add_course'),
    path('exams/', views.exam_list, name='exam_list'),
    path('attendance/', views.attendance_list, name='attendance_list'),
    path('marks/', views.marks_list, name='marks_list'),
    path('parent/', views.parent_dashboard, name='parent_dashboard'),
    path('teachers/add/', views.add_teacher, name='add_teacher'),
    path('teachers/', views.teacher_list, name='teacher_list'),

]
