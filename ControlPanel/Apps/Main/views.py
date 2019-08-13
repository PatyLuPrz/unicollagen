from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def login(request):
    return render(request, 'Main/login.html')

@login_required
def menu(request):
    return render(request, 'Main/menu.html')