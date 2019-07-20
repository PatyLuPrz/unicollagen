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
    # producto = Espanol.objects.get(id = id_producto)
    translate_client = translate.Client.from_service_account_json('keys.json')
    # nombre = producto['nombre_producto']
    # print (nombre)
    # traduccion = translate_client.translate(nombre)
    # marca = translate_client.translate(producto['marca_producto'])
    # print(nombre)
    # print(marca)

    # Espanol.objects.get(id = id_producto)
    cadena = ""
    producto = Espanol.objects.get(id=id_producto)
    print(type(producto))
    print(dir(producto))
    print(producto)
    marca = producto.marca_producto
    traduccion = translate_client.translate(marca)
    print(traduccion)
    print(type(traduccion))
    cadena = "Texto original: "+traduccion['input']+"\n Texto traducido: "+traduccion['translatedText']
    
    nombre_producto = translate_client.translate(producto.nombre_producto)
    marca_producto = translate_client.translate(producto.marca_producto)
    presentacion_producto = translate_client.translate(producto.presentacion_producto)
    descripcion = translate_client.translate(producto.presentacion_producto)

    dicc = {'nombre':nombre_producto['translatedText'],
    'marca':marca_producto['translatedText'],
    'presentacion':presentacion_producto['translatedText'],
    'descripcion':descripcion['translatedText']
    }

    contexto = {'dicc':dicc}

    return render(request, 'Productos/ingles_insert.html', contexto)