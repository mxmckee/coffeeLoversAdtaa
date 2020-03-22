"""coffeeLoversAdtaa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from invitations import views as invitation_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('changepassword/', user_views.change_password, name='changepassword'),
    path('login/', user_views.AdtaaLoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
    path('userlist/', user_views.UserListView.as_view(template_name='users/userlist.html'), name='userlist'),
    path('user/<int:pk>/', user_views.UserDetailView.as_view(template_name='users/AdtaaUser_detail.html'), name='user-detail'),
    path('user/<int:pk>/update/', user_views.UserUpdateView.as_view(template_name='users/user_form.html'), name='user-update'),
    path('accept-invite/', user_views.root_register, name='account_signup'),
    path('user/rootinvite/', user_views.RootInvite, name='rootinvite'),
    path('user/rootinviteview/', user_views.RootInviteView.as_view(template_name='users/rootinvitelist.html'), name='rootinviteview'),
    path('user/rootinvitechange/', user_views.RootInviteChange, name='rootinvitechange'),
    path('user/<int:pk>/rootinviteupdate', user_views.RootInviteDetail.as_view(template_name='users/root_invite_detail.html'), name='invite-detail'),


    path('', include('Adtaa.urls')),

    url(r'^invitations/', include('invitations.urls', namespace='invitations')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
