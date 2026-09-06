from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from django.contrib import messages
from .forms import ItemEntryForm




def list_reports(request):
    items = Item.objects.all()
    return render(request, 'dashboard.html', {'items': items})

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
    print(report)
    return render(request, 'detail.html', {'report': report})


def report_update(request, pk):
    report = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        report = ItemEntryForm(request.POST, instance=report)
        if report.is_valid():
            report.save()
            return redirect(f'report_detail/{pk}')
    else:
        report = ItemEntryForm(instance=report)

    return redirect('report_detail', pk=pk)   



def report_delete():
    # Delete the specific object
    Item.delete()   
    pass

def my_reports():
    pass