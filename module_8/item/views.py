from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from django.contrib import messages
from .forms import ItemEntryForm, ItemStatusForm
from django.db.models import Q


def list_reports(request):
    items = Item.objects.all()
    q = request.GET.get('q', '').strip()
    if q:
        items = items.filter(name__icontains=q)
    return render(request, 'dashboard.html', {'items': items})   

# def list_reports(request):
#     items = Item.objects.all()
#     return render(request, 'dashboard.html', {'items': items})

def item_create(request):
    if request.method =='POST':
        form = ItemEntryForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('dashboard')
    else:
        form = ItemEntryForm()
    return render(request, 'entry.html', {'form': form})


def report_detail(request, pk):
    report = get_object_or_404(Item,pk=pk)   
    return render(request, 'detail.html', {'report': report})


def report_update(request, pk):
    report = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemStatusForm(request.POST, instance=report)
        if form.is_valid():
            form.save()
            return redirect('report_detail', pk=pk)
    else:
        form = ItemStatusForm(instance=report)
    return render(request, 'update.html', {'form': form, 'report': report})     



def report_delete(request, pk):
    report = get_object_or_404(Item, pk=pk)
    if report.user != request.user:
        return redirect('dashboard')
    if request.method == 'POST':
        report.delete()
        return redirect('dashboard')
    return render(request, 'delete.html', {'report': report})

def my_reports(request):
    reports = Item.objects.filter(user=request.user)
    return render(request, 'my_reports.html', {'reports': reports})