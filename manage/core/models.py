from django.db import models
from django.contrib.auth.models import AbstractUser

class College(models.Model):
    college_name = models.CharField(max_length=50)

    def __str__(self):
        return self.college_name

class Department(models.Model):
    name = models.CharField(max_length=50)
    college = models.ForeignKey(College, related_name='departments', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Course(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    credit = models.IntegerField()
    prerequisite = models.ManyToManyField('self', symmetrical=False, related_name='subsequent_courses')
    department = models.ForeignKey(Department, related_name='courses', on_delete=models.CASCADE)
    semester = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.code}-{self.name}"
    
    def save(self, *args, **kwargs):
        if int(self.code.split('-')[1]) % 2 == 0:
            self.semester = 'Second Semester'
        else:
            self.semester = 'First Semester'
        super().save(*args, **kwargs)

class User(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('reistrar', 'Registrar'),
        ('department_head', 'Department Head'),
        #('admin', 'Admin'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)



class Student(models.Model):
    id = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=30) 
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))
    year = models.IntegerField(default = 0)
    semester = models.CharField(max_length=1, choices=(('I', 'semester 1'), ('II', 'semester 2')))
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=123)

    def __str__(self):
        return self.name

"""class Admin(models.Model):
    ID = models.CharField(max_length=15)
    password = models.CharField(max_length=50)"""

class Teacher(models.Model):
    Id = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Registrar(models.Model):
    Id = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


