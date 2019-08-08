from django.shortcuts import render
from django.http import HttpResponse
from Apps.Ventas.models import Venta, Detalle, Direccion, Cliente
from Apps.Productos.models import Espanol, Existencia
# Create your views here.

def index(request):
    ventas = Venta.objects.all()
    detalle = Detalle.objects.all()
    direccion = Direccion.objects.all()
    contexto = {'ventas':ventas,'detalle':detalle,'direccion':direccion}
    return render(request, 'Ventas/index.html',contexto)

def view(request,id_venta):
    ventas = Venta.objects.get(id=id_venta)
    # detalle = Detalle.objects.filter(id=id_venta).values()
    # lista_detalle = list(detalle)
    # print(lista_detalle)
    # print(type(lista_detalle))
    # print(type(lista_detalle[0]))
    # dicc = lista_detalle[0]
    # print(lista_detalle[0])
    # print(dicc)
    # print(type(dicc))
    # print(dir(dicc))
    # print(dicc['venta_id'])
    
    # detalle = Detalle.objects.get(venta_id = id_venta)
    detalle = Detalle.objects.filter(venta_id=id_venta).values()
    print(detalle)
    print(dir(detalle))
    print(type(detalle))
    lista_productos = []
    for x in detalle:
        cadena = x['producto_id']
        lista_productos.append(cadena)
        print(x['producto_id'])
        print('----')

    print(lista_productos)
    otherList = []
    for y in lista_productos:
        QueryProductos = Espanol.objects.get(id=y)
        otherList.append(QueryProductos)
    print('#####')
    print(type(otherList))
    print(dir(otherList))
    print(otherList)
    print('********')
    for i in otherList:
        print(i)
    # producto_id = '1'
    # productos = Espanol.objects.get(id=producto_id)
    # detalle = Detalle.objects.get(id=id_producto)
    cliente_id = ventas.cliente_id
    direccion_envio_venta_id = ventas.id
    direccion = Direccion.objects.filter(id=direccion_envio_venta_id).values()
    cliente = Cliente.objects.filter(id=cliente_id).values()
    contexto = {'ventas':ventas,'detalle':detalle,'direccion':direccion,'cliente':cliente,'productos':otherList}
    return render(request, 'Ventas/view.html', contexto)