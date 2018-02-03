# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Categoria(models.Model):
    categoria=models.CharField(max_length=1000)

class Usuario(models.Model):
    nombre=models.CharField(max_length=1000)
    apellido=models.CharField(max_length=1000)
    pais=models.CharField(max_length=1000)
    ciudad=models.CharField(max_length=1000)
    direccion=models.CharField(max_length=1000)
    correo=models.CharField(max_length=1000)
    categorias = models.ManyToManyField(Categoria)

class Promocion(models.Model):
    nombre=models.CharField(max_length=1000)
    imagen=models.CharField(max_length=1000)
    descripcion = models.CharField(max_length=1000)
    valor = models.IntegerField(default=0)
    fecha = models.DateField
    categoria=models.OneToOneField(Categoria,on_delete=models.CASCADE)

class Comentario(models.Model):
    comentario=models.CharField(max_length=1000)
    promocion=models.ForeignKey(Promocion, on_delete=models.CASCADE)
    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)






