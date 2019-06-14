from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'Productos/index.html')

def insert(request):
    return render(request, 'Productos/insert.html')

def view(request):
    return render(request, 'Productos/view.html')

def update(request):
    return render(request, 'Productos/update.html')

def delete(request):
    return render(request, 'Productos/delete.html')

