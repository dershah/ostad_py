from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Blog
from .forms import BlogForm
from django.db.models import Q

# - - - - - All Blogs - - - - -
def allblogs_view(request):
    blogs =Blog.objects.all()
    render(request, 'homepage.html', {'blogs':blogs})

def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            messages.success(request, "Blog has been created Successfully")
            return redirect('homepage')
    else:
        form = BlogForm()

    return render(request, 'create_blog.html', {'form':form})