from django.shortcuts import render, redirect
from django.http import HttpResponse
from Apps.Productos.models import Espanol, Ingles, Precio, Existencia, Presentacion
from Apps.Productos.forms import EspanolForm, InglesForm, PreciosForm, StockForm, PresentacionForm
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
        return redirect('/productos')
    else:
        form = EspanolForm()
    return render(request, 'Productos/insert.html',{'form':form})

def view(request, id_producto):
    producto = Espanol.objects.get(id = id_producto)
    try:
        ingles = Ingles.objects.get(producto_id = id_producto)
    except Ingles.DoesNotExist as a:
        print("Error al encontrar coincidencias(ingles): ",a.args)
        ingles = None
    try:
        precios = Precio.objects.get(producto_id = id_producto)
    except Precio.DoesNotExist as c:
        print("Error al encontrar coincidencias(precio): ",c.args)
        precios = None
    try:
        stock = Existencia.objects.get(producto_id = id_producto)
    except Existencia.DoesNotExist as d:
        print("Error al encontrar coincidencias(existencias): ",d.args)
        stock = None
    try:
        presentacion = Presentacion.objects.filter(producto_id = id_producto)
    except Presentacion.DoesNotExist as e:
        print("Error al encontrar coincidencias(presentacion): ",e.args)
        presentacion = None
    contexto = {'producto':producto,'ingles':ingles,'precios':precios,'stock':stock,'presentacion':presentacion}
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

def delete(request,id_producto):
    producto = Espanol.objects.get(id = id_producto)
    if request.method == 'POST':
        producto.delete()
        return redirect('/productos')
    return render(request, 'Productos/delete.html',{'producto':producto})


    return render(request, 'Productos/delete.html')

def ingles(request,id_producto):
    if request.method == 'GET':     
        print('GET - ingles')
        dicc = TraducirIngles(id_producto)
        contexto = {'productos':dicc}
        return render(request, 'Productos/ingles_insert.html', contexto)
    else:
        print('POST - ingles')
        datos = TraducirIngles(id_producto)
        nombre = datos['nombre']
        marca = datos['marca']
        tipo = datos['tipo']
        descripcion = datos['descripcion']
        recomendacion = datos['recomendacion']
        beneficios = datos['beneficios']
        form = Ingles(nombre_producto_ingles = nombre, marca_producto_ingles = marca, tipo_producto_ingles = tipo, descripcion_producto_ingles = descripcion, recomendacion_producto_ingles = recomendacion ,beneficios_producto_ingles = beneficios ,producto_id = int(id_producto))
        try:
            form.save()
            print("Correcto")
            return redirect('/productos')
        except Exception as e:
            print("Algo salio mal")
            print(e.args)
            return redirect('/error-fk')
    return render(request, 'Productos/ingles_insert.html', contexto)

def TraducirIngles(id_producto):
    translate_client = translate.Client.from_service_account_json('keys.json')
    producto = Espanol.objects.get(id=id_producto)
    marca = producto.marca_producto
    traduccion = translate_client.translate(marca)

    tipo_producto = producto.tipo_producto
    
    nombre_producto = translate_client.translate(producto.nombre_producto)
    marca_producto = translate_client.translate(producto.marca_producto)
    descripcion_producto = translate_client.translate(producto.descripcion_producto)
    recomendacion_producto = translate_client.translate(producto.recomendacion_producto) 
    beneficios_producto = translate_client.translate(producto.beneficios_producto)

    dicc = {
        'nombre':nombre_producto['translatedText'],
        'marca':marca_producto['translatedText'],
        'tipo':tipo_producto,
        'descripcion':descripcion_producto['translatedText'],
        'recomendacion':recomendacion_producto['translatedText'],
        'beneficios':beneficios_producto['translatedText'],
    }

    return dicc


def otheringlesinsert(request):
    if request.method == 'POST':
        form = InglesForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/productos/')
    else:
        form = InglesForm()
    return render(request, 'Productos/insert_ingles_normal.html',{'form':form})

def otheringlesupdate(request,id_producto):
    producto = Ingles.objects.get(producto_id = id_producto)
    if request.method == 'GET':
        form = InglesForm(instance=producto)
    else:
        form = InglesForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
        return redirect('/productos')
    return render(request, 'Productos/update.html', {'form':form})

def insertPrecios(request):
    if request.method == 'POST':
        form = PreciosForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/productos/')
    else:
        form = PreciosForm()
    return render(request, 'Productos/insert_precios.html',{'form':form})

def updatePrecios(request,id_producto):
    precios = Precio.objects.get(producto_id = id_producto)
    if request.method == 'GET':
        form = PreciosForm(instance=precios)
    else:
        form = PreciosForm(request.POST, instance=precios)
        if form.is_valid():
            form.save()
        return redirect('/productos')
    return render(request, 'Productos/update_precios.html', {'form':form})

def insertStock(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/productos')
    else:
        form = StockForm()
    return render(request, 'Productos/insert_stock.html',{'form':form})

def updateStock(request,id_producto):
    stock = Existencia.objects.get(producto_id = id_producto)
    if request.method == 'GET':
        form = StockForm(instance=stock)
    else:
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            form.save()
        return redirect('/productos')
    return render(request, 'Productos/update_stock.html', {'form':form})

def insertPresentacion(request):
    if request.method == 'POST':
        form = PresentacionForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/productos')
    else:
        form = PresentacionForm()
    return render(request, 'Productos/insert_presentacion.html',{'form':form})

def updatePresentacion(request,id):
    presentacion = Presentacion.objects.get(id = id)
    if request.method == 'GET':
        form = PresentacionForm(instance=presentacion)
    else:
        form = PresentacionForm(request.POST, instance=presentacion)
        if form.is_valid():
            form.save()
        return redirect('/productos')
    return render(request, 'Productos/update_presentacion.html', {'form':form})

def deletePresentacion(request,id):
    presentacion = Presentacion.objects.get(id = id)
    if request.method == 'POST':
        presentacion.delete()
        return redirect('/productos')
    return render(request, 'Productos/delete_presentacion.html',{'presentacion':presentacion})
