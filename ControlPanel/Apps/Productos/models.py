from django.db import models

# Create your models here.

class Espanol(models.Model):
    foto_producto = models.TextField(default=None)
    nombre_producto = models.CharField(max_length=250)
    marca_producto = models.CharField(max_length=250)
    tipo_producto = models.CharField(max_length=250)
    descripcion_producto = models.TextField()
    recomendacion_producto = models.TextField()
    beneficios_producto = models.TextField()
    
    def __str__(self):
        return self.nombre_producto

class Presentacion(models.Model):
    producto = models.ForeignKey(Espanol, null = True, blank=True, on_delete = models.CASCADE)
    unidad_de_medida = models.CharField(max_length=250)
    cantidad = models.FloatField()

class Ingles(models.Model):
    nombre_producto_ingles = models.CharField(max_length=250)
    marca_producto_ingles = models.CharField(max_length=250)
    presentacion_producto_ingles = models.CharField(max_length=250)
    tipo_producto_ingles = models.CharField(max_length=250)
    descripcion_producto_ingles = models.TextField()
    recomendacion_producto_ingles = models.TextField()
    beneficios_producto_ingles = models.TextField()
    producto =  models.OneToOneField(Espanol, null=True,blank=True, on_delete=models.CASCADE)

class Existencia(models.Model):
    existencias = models.IntegerField()
    producto =  models.OneToOneField(Espanol, null=True,blank=True, on_delete=models.CASCADE)

class Precio(models.Model):
    precio_peso_mx = models.FloatField()
    precio_dolar_eua = models.FloatField()
    precio_euro = models.FloatField()
    producto =  models.OneToOneField(Espanol, null=True,blank=True, on_delete=models.CASCADE)

