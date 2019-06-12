from django.db import models

# Create your models here.


class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=250)
    apellido_paterno_usuario = models.CharField(max_length=250)
    apellido_materno_usuario = models.CharField(max_length=250)
    correo_usuario = models.EmailField()
    contrasena_usuario = models.TextField()