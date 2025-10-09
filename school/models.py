from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enrollment_number = models.CharField(max_length=20, unique=True, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    grade = models.CharField(max_length=10, null=True, blank=True)
    parent_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='children')
    courses = models.ManyToManyField('Course', blank=True)

    def __str__(self):
        return self.user.get_full_name()

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=20, unique=True, null=True, blank=True)
    courses = models.ManyToManyField('Course', blank=True, related_name='teachers')

    def __str__(self):
        return self.user.get_full_name()

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True, default='COURSE001')
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True, related_name='main_courses')

    def __str__(self):
        return self.name

class Exam(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)  # add this
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    total_marks = models.IntegerField(default=100)

    def __str__(self):
        return f"{self.name} ({self.course.name})"
class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    exam = models.ForeignKey(Exam, null=True, blank=True, on_delete=models.SET_NULL)
    marks = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.marks}"


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Present','Present'), ('Absent','Absent')])
