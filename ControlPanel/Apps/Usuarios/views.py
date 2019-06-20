from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'Usuarios/index.html')

def insert(request):
    return render(request, 'Usuarios/insert.html')

def view(request):
    return render(request, 'Usuarios/view.html')

def update(request):
    return render(request, 'Usuarios/update.html')

def delete(request):
    return render(request, 'Usuarios/delete.html')
