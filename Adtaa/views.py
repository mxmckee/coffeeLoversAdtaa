from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView, UpdateView, CreateView
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
