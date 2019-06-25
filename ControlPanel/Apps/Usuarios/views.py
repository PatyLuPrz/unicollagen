from django.shortcuts import render, redirect
from django.http import HttpResponse

from Apps.Usuarios.models import Usuario
from Apps.Usuarios.forms import UsuarioForm
# Create your views here.

def index(request):
    usuario = Usuario.objects.all()
    contexto = {'usuario':usuario}
    return render(request, 'Usuarios/index.html',contexto)

def insert(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'Usuarios/insert.html', {'form':form})

def view(request):
    return render(request, 'Usuarios/view.html')

def update(request):
    return render(request, 'Usuarios/update.html')

def delete(request):
    return render(request, 'Usuarios/delete.html')
