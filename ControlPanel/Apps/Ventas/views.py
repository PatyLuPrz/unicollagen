from django.shortcuts import render
from django.http import HttpResponse
from Apps.Ventas.models import Venta, Detalle, Direccion
from Apps.Productos.models import Espanol, Existencia
# Create your views here.

def index(request):
    ventas = Venta.objects.all()
    detalle = Detalle.objects.all()
    direccion = Direccion.objects.all()
    contexto = {'ventas':ventas,'detalle':detalle,'direccion':direccion}
    return render(request, 'Ventas/index.html',contexto)

def view(request):
    return render(request, 'Ventas/view.html')