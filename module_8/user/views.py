from django.shortcuts import render, redirect
from user.forms import user_registration_form
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import time

# Create your views here.
def register_view(request):
    if request.method == "POST":
        registration_form = user_registration_form(request.POST)
        if registration_form.is_valid():
            password = request.POST.get("password")
            confirm_password = request.POST.get("confirm_password")
            if password == confirm_password:
                registration_form.save()
                messages.success(request, "User has been registered successfully")
                return redirect('login')
            else:
                registration_form.add_error(
                    'confirm_password',
                    "Passwords do not match."
                )
    else:
        registration_form = user_registration_form()

    return render(request, 'registration.html', context={"form": registration_form})

def login_view(request):
    if request.method == "POST":
        uname  = request.POST.get("uname")
        pswd = request.POST.get("psw")
        user = authenticate(request, username=uname, password=pswd)
        print(uname, pswd)
        if user is not None:
            login(request, user)
            messages.success(request, "Log in successful")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'login.html')
    

def dashboard_view(request):
    return render(request, 'dashboard.html')

def logout_view(request):
    pass