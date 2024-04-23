from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}! You are logged in!')
            return redirect('weather_app:weather')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profilepage(request):
    return render(request, 'users/profile.html')


def custom_logout(request):
    auth_logout(request)
    # Redirect to the desired URL after logout
    return redirect('logout')


