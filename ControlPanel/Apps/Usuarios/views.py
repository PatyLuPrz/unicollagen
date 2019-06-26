from django.shortcuts import render, redirect
from django.http import HttpResponse

from Apps.Usuarios.models import Usuario
from Apps.Usuarios.forms import UsuarioForm, UsuarioNoPasswordForm
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

def update(request, id_usuario):
    usuario = Usuario.objects.get(id = id_usuario)
    if request.method == 'GET':
        form = UsuarioNoPasswordForm(instance=usuario)
    else:
        form = UsuarioNoPasswordForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
        return redirect('/usuarios')
    return render(request, 'Usuarios/update.html', {'form':form})

def delete(request, id_usuario):
    usuario = Usuario.objects.get(id = id_usuario)
    if request.method == 'POST':
        usuario.delete()
        return redirect('/usuarios')
    return render(request, 'Usuarios/delete.html', {'usuario':usuario})
