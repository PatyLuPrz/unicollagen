from django.contrib import admin
from Apps.Productos.models import Producto_espanol, Producto_frances, Producto_ingles
# Register your models here.
admin.site.register(Producto_espanol)
admin.site.register(Producto_frances)
admin.site.register(Producto_ingles)
