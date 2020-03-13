from django.shortcuts import render, redirect
from .models import AdtaaUser
from .forms import AdtaaUserForm, AdtaaAuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

def register(request):
    if request.method == 'POST':
        form=AdtaaUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.is_active=False
            user.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = AdtaaUserForm()

    return render(request, 'users/register.html', {'form':form})

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
