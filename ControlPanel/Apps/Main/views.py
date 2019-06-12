from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def login(request):
    return render(request, 'Main/login.html')

def menu(request):
    return render(request, 'Main/menu.html')