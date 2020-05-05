from django.urls import path, include
from Adtaa import views as Adtaa_views
from users import views as users_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pdf/', Adtaa_views.generatePDF_view, name='pdf'),
    path('schedcourselist/', Adtaa_views.SchedCourseListView.as_view(template_name='Adtaa/sched_courselist.html'), name='schedcourselist'),
    path('schedcourse/<int:pk>/update', Adtaa_views.SchedCourseUpdateView.as_view(template_name='Adtaa/sched_course_update_form.html'), name='sched-course-update'),
    path('courselist/', Adtaa_views.CourseListView.as_view(template_name='Adtaa/courselist.html'), name='courselist'),
    path('courseadd/', Adtaa_views.CourseAddView.as_view(template_name='Adtaa/course_form.html'), name='course-add'),
    path('course/<int:pk>/update', Adtaa_views.CourseUpdateView.as_view(template_name='Adtaa/course_update_form.html'), name='course-update'),
    path('course/<int:pk>/delete', Adtaa_views.CourseDeleteView.as_view(template_name='Adtaa/course_confirm_delete.html'), name='course-delete'),
    path('instructoradd/', Adtaa_views.InstructorAddView.as_view(template_name='Adtaa/instructor_form.html'), name='instructor-add'),
    path('instructorlist/', Adtaa_views.InstructorListView.as_view(template_name='Adtaa/instructorlist.html'), name='instructorlist'),
    path('instructor/<int:pk>/update', Adtaa_views.InstructorUpdateView.as_view(template_name='Adtaa/instructor_update_form.html'), name='instructor-update'),
    path('instructor/<int:pk>/delete', Adtaa_views.InstructorDeleteView.as_view(template_name='Adtaa/instructor_confirm_delete.html'), name='instructor-delete'),
    path('schedule/', Adtaa_views.schedule, name='schedule'),
    path('userslist/', users_views.UserListView.as_view(template_name='users/users_list.html'), name='userslist'),
    path('user/<int:pk>/delete', users_views.UserDeleteView.as_view(template_name='users/user_confirm_delete.html'), name='user-delete'),
]