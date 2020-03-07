from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Course, Instructor

#this is the views page for the adtaa

def index(request):
    return render(request, 'Adtaa/index.html')

class CourseListView(ListView):
    model = Course
    context_object_name = 'courses'

class CourseAddView(LoginRequiredMixin, CreateView):
    model = Course
    fields = ['courseNumber', 'courseTitle', 'courseDays', 'courseTime', 'instructor', 'discipline1', 'discipline2']

class CourseUpdateView(LoginRequiredMixin, UpdateView):
    model = Course
    fields = ['courseNumber', 'courseTitle', 'courseDays', 'courseTime', 'instructor', 'discipline1', 'discipline2']

class CourseDeleteView(LoginRequiredMixin, DeleteView):
    model=Course
    success_url = '/courselist'



class InstructorListView(ListView):
    model = Instructor
    context_object_name = 'instructors'

class InstructorAddView(LoginRequiredMixin, CreateView):
    model = Instructor
    fields = ['firstName', 'lastName', 'maxClassLoad', 'discipline1', 'discipline2']

class InstructorUpdateView(LoginRequiredMixin, UpdateView):
    model = Instructor
    fields = ['firstName', 'lastName', 'maxClassLoad', 'discipline1', 'discipline2']

class InstructorDeleteView(LoginRequiredMixin, DeleteView):
    model=Instructor
    success_url = '/instructorlist'