from django.shortcuts import render, redirect
from django.http import HttpResponse
from Apps.Productos.models import Espanol
from Apps.Productos.forms import EspanolForm, InglesForm
from google.cloud import translate
import json

def index(request):
    producto = Espanol.objects.all()
    contexto = {'producto':producto}
    return render(request, 'Productos/index.html', contexto)

def insert(request):
    if request.method == 'POST':
        form = EspanolForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/productos/insert/ingles')
    else:
        form = EspanolForm()
    return render(request, 'Productos/insert.html',{'form':form})

def view(request, id_producto):
    producto = Espanol.objects.get(id = id_producto)
    contexto = {'producto':producto}
    return render(request, 'Productos/view.html', contexto)

def update(request, id_producto):
    producto = Espanol.objects.get(id = id_producto)
    if request.method == 'GET':
        form = EspanolForm(instance=producto)
    else:
        form = EspanolForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
        return redirect('/productos')
    return render(request, 'Productos/update.html', {'form':form})

def delete(request):
    return render(request, 'Productos/delete.html')

def ingles(request,id_producto):
    producto = Espanol.objects.get(id = id_producto)
    translate_client = translate.Client.from_service_account_json('keys.json')
    producto['']
    hola = translate_client.translate('Estoy vivo!')
    print(hola)
    return HttpResponse(hola['translatedText'])