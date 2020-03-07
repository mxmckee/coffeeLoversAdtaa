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
    path('course/<int:pk>/update', Adtaa_views.CourseUpdateView.as_view(template_name='Adtaa/course_update_form.html'), name='course-update'),
    path('course/<int:pk>/delete', Adtaa_views.CourseDeleteView.as_view(template_name='Adtaa/course_confirm_delete.html'), name='course-delete'),
    path('instructoradd/', Adtaa_views.InstructorAddView.as_view(template_name='Adtaa/instructor_form.html'), name='instructor-add'),
    path('instructorlist/', Adtaa_views.InstructorListView.as_view(template_name='Adtaa/instructorlist.html'), name='instructorlist'),
    path('instructor/<int:pk>/update', Adtaa_views.InstructorUpdateView.as_view(template_name='Adtaa/instructor_update_form.html'), name='instructor-update'),
    path('instructor/<int:pk>/delete', Adtaa_views.InstructorDeleteView.as_view(template_name='Adtaa/instructor_confirm_delete.html'), name='instructor-delete'),
]