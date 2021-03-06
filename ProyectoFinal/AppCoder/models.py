from django.db import models
from django import forms

from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField



# Create your models here.

class Usuario (models.Model):
    nombre =  models.CharField (max_length=40)
    apellido = models.CharField(null=True,max_length=40)
    fechaNacimiento = models.DateField()
    correo = models.EmailField()
    contrasena = models.CharField(max_length=40)
    
    

    def __str__(self):
        return f"nombre:{self.nombre}"

class Pelicula (models.Model):
    nombre =  models.CharField (max_length=40)
    año = models.IntegerField (null=True)
    director = models.CharField (max_length=40,null=True )
    genero = models.CharField (max_length=40)
    duracion = models.TimeField (null=True)

    def __str__(self):
        return f"{self.nombre}({self.año})"

class Newsletter(models.Model):
    email = models.EmailField()

    def __str__(self):
      return f"{self.email}"


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)