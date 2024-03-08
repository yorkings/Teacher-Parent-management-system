from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    CHOICES = [
        ('admin', 'ADMIN'),
        ('parent', 'PARENT'),
        ('teacher', 'TEACHER')
    ]
    role = models.CharField(choices=CHOICES, default='admin', max_length=10)

class events(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(blank=True,null=True,upload_to="events")
    details=models.TextField()
    def __str__(self):
        return self.title
    
class Assignments(models.Model):
    subject=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    content=models.TextField()
    def __str__(self):
        return self.subject

class Session(models.Model):
    year = models.CharField(max_length=10)

class Subject(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    student_class = models.ForeignKey('StudentClass', on_delete=models.CASCADE)

class Student(models.Model):
    student_name = models.CharField(max_length=100)
    admission_no = models.CharField(max_length=30)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    student_class = models.ForeignKey('StudentClass', on_delete=models.CASCADE)

class StudentClass(models.Model):
    class_name = models.CharField(max_length=50)

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()
    grade = models.CharField(max_length=2)

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    is_present = models.BooleanField(default=True)