from django.urls import path
from .views import *

urlpatterns = [
    path('colleges/', CollegeListView.as_view(), name='college_list'),
    path('colleges/add/', CollegeCreateView.as_view(), name='college_add'),
    path('department/', DepartmentListView.as_view(), name='department_list'),
    path('department/add/', DepartmentCreateView.as_view(), name='department_add'),
    path('courses/', CourseListView.as_view(), name='course_list'),
    path('colleges/add/', CourseCreateView.as_view(), name='course_add'),

]
