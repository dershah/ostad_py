from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserAuthenticationForm
from .models import CustomUser

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Sign Up was Successful. Please login using your Credentials")
            return redirect('login')
    else:
        form =UserRegistrationForm()
        messages.error(request,"Sign Up was not Successful. Please recheck the Entries")
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserAuthenticationForm(request, request.POST)

        if form.is_valid():
            email= form.cleaned_data['username']
            password= form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome Back {user}")
                return redirect('profile')

    else:
        form = UserAuthenticationForm()
        messages.error(request,"Invalid Credentials")

    return render(request, 'accounts/login.html', {'form':form})

@login_required
def profile_view(request):
    profile = request.user
    return render(request, 'accounts/profile.html', {'profile': profile})   

def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')


