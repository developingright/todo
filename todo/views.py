from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.
def index(request):
    items = Task.objects.all()
    form = TodoForm()
    if request.method=='POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            print("asdds'")
            form.save()
        else:
            print("asasd")
        return redirect('/')
    context = {'items':items,'forms':form}
    return render(request, 'todo/index.html',context)

def edit(request,pk):
    item = Task.objects.get(id=pk)
    form = TodoForm(instance=item)
    if request.method=='POST':
        form = TodoForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'form':form}
    return render(request, 'todo/edit.html',context)

def delete(request,pk):
    item = Task.objects.get(id=pk)

    item.delete()
    return redirect('/')
    
