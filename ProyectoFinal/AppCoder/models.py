from django.db import models

# Create your models here.


class persona (models.Model):
    nombre =  models.CharField (max_length=40)
    apellido =  models.CharField (max_length=40)
    edad = models.IntegerField ()
    direccion =  models.CharField (max_length=40, null=True)
    
class pelicula (models.Model):
    nombre =  models.CharField (max_length=40)
    genero = models.CharField (max_length=40)
    duracion= models.IntegerField()

class series (models.Model):
    nombre =  models.CharField (max_length=40)
    genero = models.CharField (max_length=40)
    canTemportadas = models.IntegerField()



    