from django.db import models


# Create your models here.

class usuario (models.Model):
    nombre =  models.CharField (max_length=40 )
    edad = models.IntegerField ()
    direccion =  models.CharField (max_length=40)
    fechaNacimiento = models.DateField()

    def __str__(self):
        return f"nombre:{self.nombre}"

class pelicula (models.Model):
    nombre =  models.CharField (max_length=40)
    año = models.IntegerField (null=True)
    director = models.CharField (max_length=40,null=True )
    genero = models.CharField (max_length=40)
    duracion = models.IntegerField (null=True)

    def __str__(self):
        return f"{self.nombre}({self.año})"


class usuarioNewsletter (models.Model):
    email = models.EmailField(null=True)

    def __str__(self):
        return f"{self.email}"
