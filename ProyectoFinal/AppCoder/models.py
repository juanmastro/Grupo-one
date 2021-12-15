from django.db import models

# Create your models here.

class usuario (models.Model):
    nombre =  models.CharField (max_length=40)
    fechaNacimiento = models.DateField()

class pelicula (models.Model):
    nombre =  models.CharField (max_length=40)
    año = models.IntegerField (max_length=4)
    director = models.CharField (max_length=40)
    genero = models.CharField (max_length=40)

class usuarioNewsletter (models.Model):
    email = models.EmailField()
