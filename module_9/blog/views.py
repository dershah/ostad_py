from django.shortcuts import render,redirect, get_object_or_404
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

def blog_detail(request, pk):
    blog =get_object_or_404(Blog, pk=pk)
    return render(request, 'blog.html', {'blog': blog})

def blog_update(request,pk):
    blog =get_object_or_404(Blog, pk=pk)
    if blog.author != request.user:
        messages.error(request, 'You are not allowed to update/ delete this post')
        return redirect('homepage')
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect ('blog',pk=pk)
    else:
        form = form = BlogForm(request.POST, instance=blog)
    return render(request, 'update.html', {'form': form, 'blog': blog})

def blog_delete(request):
    pass

def my_blogs(request):
    pass