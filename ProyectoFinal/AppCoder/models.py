from django.db import models

# Create your models here.

class usuario (models.Model):
    nombre =  models.CharField (max_length=40)
    edad = models.IntegerField (null=True)
    direccion =  models.CharField (max_length=40,)
    fechaNacimiento = models.DateField(null=True)

class pelicula (models.Model):
    nombre =  models.CharField (max_length=40)
    año = models.IntegerField (null=True)
    director = models.CharField (max_length=40,null=True )
    genero = models.CharField (max_length=40)
    duracion = models.IntegerField (null=True)

class serie (models.Model):
    nombre =  models.CharField (max_length=40)
    año = models.IntegerField (null=True)
    genero = models.CharField (max_length=40)
    cantemporadas = models.IntegerField (null=True)


class usuarioNewsletter (models.Model):
    email = models.EmailField(null=True)
