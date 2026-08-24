from django.shortcuts import render
from .models import project

def homepage(request):
    return render(request, 'homepage.html')

def all_projects(request):
    projects = project.objects.all()
    context={
        'projects': projects
    }
    
    return render(request, 'projects.html', context)