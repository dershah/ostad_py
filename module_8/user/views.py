from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import user_registration_form, user_authentication_form


def register_view(request):
    if request.method == 'POST':
        form = user_registration_form(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = user_registration_form()
    return render(request, 'registration.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = user_authentication_form(request, request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            print(f"User: {user}")
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back {user}')
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid credentials.')
    else:
        form = user_authentication_form() 
    return render(request, 'login.html', {'form': form})

@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')

def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')
