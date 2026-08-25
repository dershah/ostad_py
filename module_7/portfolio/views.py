from django.shortcuts import render,get_object_or_404
from .models import project

def homepage(request):
    return render(request, 'homepage.html')

def all_projects(request):
    projects = project.objects.all()
    context={
        'projects': projects
    }
    
    return render(request, 'projects.html', context)
def about_me(request):
    return render(request, 'about.html')

def project_detail(request, pk):
    project_details = get_object_or_404(project, pk=pk)
    
    context = {
        "project": project_details
    }
    return render(request, "project.html", context)