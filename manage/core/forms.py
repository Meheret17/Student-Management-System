from django import forms
from .models import College, Department, Course

class CollegeForm(forms.ModelForm):
    class Meta:
        model = College
        fields = ['name']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'college']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'department', 'code']
