from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'Productos/index.html')

def insert(request):
    return render(request, 'Productos/insert.html')

def new(request):
    return render(request, 'Productos/new.html')