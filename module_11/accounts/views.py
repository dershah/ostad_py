from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserAuthenticationForm, UserProfileEditForm
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
            messages.error(request, "Sign Up was not Successful. Please recheck the Entries")
    else:
        form = UserRegistrationForm()
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
                messages.success(request, f"Welcome Back {user.email}")
                return redirect('profile')

    else:
        form = UserAuthenticationForm()

    return render(request, 'accounts/login.html', {'form':form})

@login_required
def profile_view(request):
    profile = request.user
    user_properties = []
    if profile.is_owner:
        user_properties = profile.properties.prefetch_related('images').all()

    return render(request, 'accounts/profile.html', {
        'profile': profile,
        'user_properties': user_properties,
    })

@login_required
def profile_edit_view(request):
    if request.method == 'POST':
        form = UserProfileEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated successfully.")
            return redirect('profile')
    else:
        form = UserProfileEditForm(instance=request.user)

    return render(request, 'accounts/profile_edit.html', {
        'form': form,
    })

def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')




