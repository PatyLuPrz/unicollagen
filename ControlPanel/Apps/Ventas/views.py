from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'Ventas/index.html')

def view(request):
    return render(request, 'Ventas/view.html')