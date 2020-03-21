from django.shortcuts import render, redirect
from .models import AdtaaUser
from invitations.views import SendInvite
from invitations.forms import InvitationAdminAddForm, InvitationAdminChangeForm
from .forms import AdtaaUserForm, AdtaaAuthenticationForm, AdtaaRootUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

def register(request):
    if request.method == 'POST':
        form=AdtaaUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.is_active=False
            user.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Registration request sent to Admin. You will receive an email once your account has been approved')
            return redirect('login')
    else:
        form = AdtaaUserForm()

    return render(request, 'users/register.html', {'form':form})

def root_register(request):
    if request.method == 'POST':
        form=AdtaaRootUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.is_active=True
            user.is_staff=True
            user.is_superuser=True
            user.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Welcome new root user!')
            return redirect('login')
    else:
        form = AdtaaRootUserForm()

    return render(request, 'users/account_signup.html', {'form':form})

def RootInvite(request):
    if request.method == 'POST':
        form=InvitationAdminAddForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            messages.success(request, f'Invite sent!')
            return redirect('rootinvite')
    else:
        form = InvitationAdminAddForm()

    return render(request, 'users/rootinvite.html', {'form':form})

def RootInviteChange(request):
    if request.method == 'POST':
        form=InvitationAdminChangeForm(request.POST)
        if form.is_valid():
            #user=form.save()
            #user.save()
            #messages.success(request, f'Invite sent!')
            return redirect('profile')
    else:
        form = InvitationAdminChangeForm()

    return render(request, 'users/profile.html', {'form':form})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)

            return redirect('profile')
        else:
            return redirect('changepassword')

    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, 'users/passwordchange.html', {'form':form})

@login_required()
def profile(request):
    return render(request, 'users/profile.html')

class AdtaaLoginView(LoginView):
    authentication_form = AdtaaAuthenticationForm

class UserListView(ListView):
    model = AdtaaUser
    context_object_name = 'users'
    ordering = ['-date_joined']

class UserDetailView(DetailView):
    model = AdtaaUser

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = AdtaaUser
    fields = ['is_active', 'is_staff', 'is_superuser']
