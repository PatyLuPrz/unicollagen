from django.db import models
from Apps.Productos.models import Espanol
# Create your models here.


class Direccion(models.Model):
    calle_direccion = models.CharField(max_length=255)
    colonia_direccion = models.CharField(max_length=255)
    numero_ext_direccion = models.CharField(max_length=15)
    numero_int_direccion = models.CharField(max_length=15)
    ciudad_direccion = models.CharField(max_length=255)
    estado_direccion = models.CharField(max_length=255)
    pais_direccion = models.CharField(max_length=255)
    codigo_postal_direccion = models.CharField(max_length=8)

class Cliente(models.Model):
    nombre_cliente = models.CharField(max_length=255)
    apellido_paterno_cliente = models.CharField(max_length=255)
    apellido_materno_cliente = models.CharField(max_length=255)
    correo_cliente = models.EmailField()

class Venta(models.Model):
    total_a_pagar_venta = models.FloatField()
    total_productos_venta = models.IntegerField()
    direccion_envio_venta = models.OneToOneField(Direccion, null = True, on_delete = models.CASCADE)
    cliente = models.ForeignKey(Cliente, null = True, on_delete = models.CASCADE)

class Detalle(models.Model):
    venta = models.ForeignKey(Venta, null = True, on_delete = models.CASCADE)
    producto = models.ForeignKey(Espanol, null = True, on_delete = models.CASCADE)
    existencia = models.IntegerField()
    