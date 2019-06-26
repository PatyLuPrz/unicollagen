from django.shortcuts import render, redirect

from django.http import HttpResponse

from Apps.Productos.forms import EspanolForm
# Create your views here.


def index(request):
    return render(request, 'Productos/index.html')

def insert(request):
    if request.method == 'POST':
        form = EspanolForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/productos')
    else:
        form = EspanolForm()

    return render(request, 'Productos/insert.html',{'form':form})

def view(request):
    return render(request, 'Productos/view.html')

def update(request):
    return render(request, 'Productos/update.html')

def delete(request):
    return render(request, 'Productos/delete.html')

