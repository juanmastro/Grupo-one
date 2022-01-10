from django.shortcuts import render
from django.http import HttpResponse, response    
from datetime import datetime
from django.template import Template, Context
from django.template import loader

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *
from AppCoder.models import *






# Create your views here.

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def formulario(request,):
    return render(request,"AppCoder/formulario.html")

def sobreNosotrxs(request):
    return render(request, "AppCoder/sobrenosotrxs.html")

def post1(request):
    return render(request, "AppCoder/post1.html")

def contacto(request):
    return render(request, "AppCoder/contacto.html")

def userFormulario(request):

    if request.method == "POST":

        miFormulario = UsuarioForm (request.POST)
        if miFormulario.is_valid(): 
            userInsta = Usuario (nombre=request.POST["nombre"], apellido=request.POST["apellido"],fechaNacimiento = request.POST["fechaNacimiento"],correo=request.POST["correo"], contrasena=request.POST["contrasena"]  )  
            userInsta.save() #Guarda en la base de datos

        return render(request, "AppCoder/registrook.html")
    
    else:
        miFormulario = UsuarioForm()


    return render(request, 'AppCoder/userFormulario.html', {"miFormulario":miFormulario})

def proponerPeli(request):
    return render(request, "AppCoder/proponerPeli.html")

def Newsletter(request):

    if request.method == "POST":

        formularioNewsletter = FormNewsletter(request.POST)

        if formularioNewsletter.is_valid():

            newsletterInsta = Newsletter(email=request.POST["email"])

            newsletterInsta.save()

        return render(request, "AppCoder/inicio.html")

    else:

        formularioNewsletter = FormNewsletter()

    return render(request, "AppCoder/newsletter.html", {"formularioNewsletter":formularioNewsletter})

def peliFormulario(request):

    if request.method == 'POST':

        formularioPelicula = PeliculaForm(request.POST)

        if formularioPelicula.is_valid():
            userPeli = Pelicula (nombre=request.POST["nombre"], año=request.POST["año"],director = request.POST["director"], genero=request.POST["genero"], duracion=request.POST["duracion"]  )  
            userPeli.save()

        return render(request, 'AppCoder/inicio.html')
    
    else:

        formularioPelicula = PeliculaForm()


    return render(request, 'AppCoder/peliFormulario.html', {"formularioPelicula":formularioPelicula})




def busquedapeli (request):
    return render(request, "AppCoder/busquedapeli.html")


def buscar (request):

    if request.GET ["nombre"]:
        
        nombre = request.GET ["nombre"]
        peliculas = Pelicula.objects.filter(nombre__icontains=nombre)

        return render (request, "AppCoder/resultadobusqueda.html", {"peliculas":peliculas, "nombre":nombre})

    else:
        respuesta = "No tengo informacion cargada"
    
    return HttpResponse (respuesta)
    
def resultadobusqueda (request):
    return render(request, "AppCoder/resultadobusqueda.html")


def leerpeliculas (request):

    peliculas = Pelicula.objects.all()
    dir = {"peliculas":peliculas}
    return render (request, "AppCoder/leerpeliculas.html", dir)


 


