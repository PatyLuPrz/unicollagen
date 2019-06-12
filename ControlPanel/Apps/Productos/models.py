from django.db import models

# Create your models here.

class Producto_espanol(models.Model):
    nombre_producto = models.CharField(max_length=250)
    precio_producto = models.FloatField()
    marca_producto = models.CharField(max_length=250)
    presentacion_producto = models.CharField(max_length=250)
    tipo_producto = models.CharField(max_length=250)
    descripcion_producto = models.TextField()
    recomendacion_producto = models.TextField()
    beneficios_producto = models.TextField()

class Producto_ingles(models.Model):
    nombre_producto_ingles = models.CharField(max_length=250)
    precio_producto_ingles = models.FloatField()
    marca_producto_ingles = models.CharField(max_length=250)
    presentacion_producto_ingles = models.CharField(max_length=250)
    tipo_producto_ingles = models.CharField(max_length=250)
    descripcion_producto_ingles = models.TextField()
    recomendacion_producto_ingles = models.TextField()
    beneficios_producto_ingles = models.TextField()
    producto =  models.OneToOneField(Producto_espanol, null=True,blank=True, on_delete=models.CASCADE)


class Producto_frances(models.Model):
    nombre_producto_frances = models.CharField(max_length=250)
    precio_producto_frances = models.FloatField()
    marca_producto_frances = models.CharField(max_length=250)
    presentacion_producto_frances = models.CharField(max_length=250)
    tipo_producto_frances = models.CharField(max_length=250)
    descripcion_producto_frances = models.TextField()
    recomendacion_producto_frances = models.TextField()
    beneficios_producto_frances = models.TextField()
    producto =  models.OneToOneField(Producto_espanol, null=True,blank=True, on_delete=models.CASCADE)

class Existencias(models.Model):
    existencias = models.IntegerField()
    producto =  models.OneToOneField(Producto_espanol, null=True,blank=True, on_delete=models.CASCADE)

