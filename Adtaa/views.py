from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Course, Instructor, ScheduledCourse
from Adtaa import auto_solutions_generator as coffeeFx

#this is the views page for the adtaa

def index(request):
    return render(request, 'Adtaa/index.html')

def schedule(request):

    if request.method == 'POST':
        coursesQuerySet = ScheduledCourse.objects.all()
        courses = coursesQuerySet[::1]
        coursesToSave = []
        for course in courses:
            if str(course.scheduleNumber) in request.POST:
                coursesToSave.append(course)
        ScheduledCourse.objects.all().delete()
        for course in coursesToSave:
            course.save()
        return redirect('index')


    # ScheduledCourse.objects.all().delete()
    autosolutions = coffeeFx.main()
    context = {'autosolutions': autosolutions}
    for i in range(len(autosolutions)):
        for j in range(len(autosolutions[i])):
            tempCourse = ScheduledCourse(courseNumber=autosolutions[i][j][0].courseNumber, courseTitle=autosolutions[i][j][0].courseTitle, \
                                         courseDays=autosolutions[i][j][0].courseDays, courseTime=autosolutions[i][j][0].courseTime, \
                                         instructor=autosolutions[i][j][1], scheduleNumber=i+1)
            tempCourse.save()



    return render(request, 'Adtaa/schedule.html', context)



class CourseListView(ListView):
    model = Course
    context_object_name = 'courses'

class CourseAddView(LoginRequiredMixin, CreateView):
    model = Course
    fields = ['courseNumber', 'courseTitle', 'courseDays', 'courseTime', 'discipline1', 'discipline2']

class CourseUpdateView(LoginRequiredMixin, UpdateView):
    model = Course
    fields = ['courseNumber', 'courseTitle', 'courseDays', 'courseTime', 'discipline1', 'discipline2']

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