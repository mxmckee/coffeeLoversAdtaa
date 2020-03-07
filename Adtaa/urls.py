from django.urls import path, include
from Adtaa import views as Adtaa_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('courselist/', Adtaa_views.CourseListView.as_view(template_name='Adtaa/courselist.html'), name='courselist'),
    path('courseadd/', Adtaa_views.CourseAddView.as_view(template_name='Adtaa/course_form.html'), name='course-add'),
]