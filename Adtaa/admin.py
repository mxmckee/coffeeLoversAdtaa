from django.contrib import admin
from .models import Course, Instructor, ScheduledCourse

admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(ScheduledCourse)