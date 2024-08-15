from django.shortcuts import render, redirect
from django.views import View
from .models import College, Department, Course
from .forms import CollegeForm, DepartmentForm, CourseForm

class CollegeListView(View):
    def get(self, request):
        colleges = College.objects.all()
        return render(request, 'college_list.html',{'colleges':Colleges})

class CollegeCreateView(View):
    def get(self, request):
        form = CollegeForm()
        return render(request, 'college_form.html', {'form': form})
    
    def post(self, request):
        form = CollegeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('college_list')
        return render(request, 'college_form.html', {'form': form})

class DepartmentListView(View):
    def get(self, request):
        department = Department.objects.all()
        return render(request, 'department_list.html',{'department':Department})

class DepartmentCreateView(View):
    def get(self, request):
        form = DepartmentForm()
        return render(request, 'department_form.html', {'form':form})
    
    def post(self, request):
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')
        return render(request, 'department_form.html', {'form':form})
    
class CourseListView(View):
    def get(self, request):
        course = Course.objects.all()
        return render(request, 'course_list.html',{'course':Course})

class CourseCreateView(View):
    def get(self, request):
        form = CourseForm()
        return render(request, 'course_form.html', {'form': form})
    
    def post(self, request):
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
        return render(request, 'course_form.html', {'form': form})

