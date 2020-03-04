from django.shortcuts import render, redirect
from .models import AdtaaUser
from .forms import AdtaaUserForm, AdtaaAuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

def register(request):
    if request.method == 'POST':
        form=AdtaaUserForm(request.POST)
        if form.is_valid():
            form.save()
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

