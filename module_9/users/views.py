from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import user_registration_form, user_authentication_form

def signup_view(request):
    if request.method == 'POST':
        form = user_registration_form(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Sign Up was Successful. Please login using your Credentials")
            return redirect('login')
    else:
        form =user_registration_form()
        messages.error(request,"Sign Up was not Successful. Please recheck the Entries")
    return render(request, 'registration.html', {'form': form})

def signin_view(request):
    if request.method == 'POST':
        form = user_authentication_form(request, request.POST)

        if form.is_valid():
            email= form.cleaned_data['username']
            password= form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome Back {user}")
                return redirect('dashboard')

    else:
        form = user_authentication_form()
        messages.error(request,"Invalid Credentials")

    return render(request, 'login.html', {'form':form})


@login_required
def homepage_view(request):
    return render(request, 'homepage.html')

def signout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')


