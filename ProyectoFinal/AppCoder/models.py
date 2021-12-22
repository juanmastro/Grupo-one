from django.db import models
from django import forms


# Create your models here.

class usuario (models.Model):
    nombre =  models.CharField (max_length=40)
    apellido = models.CharField(null=True,max_length=40)
    fechaNacimiento = models.DateField()
    email = models.EmailField(default='email')
    contrasena = models.CharField(max_length=40)
    

    def __str__(self):
        return f"nombre:{self.nombre}"

class pelicula (models.Model):
    nombre =  models.CharField (max_length=40)
    año = models.IntegerField (null=True)
    director = models.CharField (max_length=40,null=True )
    genero = models.CharField (max_length=40)
    duracion = models.TimeField (null=True)

    def __str__(self):
        return f"{self.nombre}({self.año})"

class newsletter(models.Model):
    email = models.EmailField()
    def __str__(self):
        return f"{self.email}"
