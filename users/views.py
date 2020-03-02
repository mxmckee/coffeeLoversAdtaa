from django.shortcuts import render, redirect
from .models import AdtaaUser
from .forms import AdtaaUserForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form=AdtaaUserForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('index')
    else:
        form = AdtaaUserForm()

    return render(request, 'users/register.html', {'form':form})

