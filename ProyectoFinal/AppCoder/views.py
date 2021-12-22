from django.shortcuts import render
from django.http import HttpResponse    
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
            userInsta = usuario (nombre=request.POST["nombre"], apellido=request.POST["apellido"],fechaNacimiento = request.POST["fechaNacimiento"], contrasena=request.POST["contrasena"]  )  
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

            newsletterInsta = newsletter(email=request.POST["email"])

            newsletterInsta.save()

        return render(request, "AppCoder/inicio.html")

    else:

        formularioNewsletter = FormNewsletter()

    return render(request, "AppCoder/newsletter.html", {"formularioNewsletter":formularioNewsletter})

def peliFormulario(request):

    if request.method == 'POST':

        formularioPelicula = PeliculaForm(request.POST)

        if formularioPelicula.is_valid():

            informacion = formularioPelicula.cleaned_data

            peli = PeliculaForm(

                nombre = informacion["nombre"],
                año = informacion["año"],
                director = informacion["director"],
                genero = informacion["genero"],
                duracion = informacion["duracion"],
            )


            peli.save()

        return render(request, 'AppCoder/inicio.html')
    
    else:

        formularioPelicula = PeliculaForm()


    return render(request, 'AppCoder/peliFormulario.html', {"formularioPelicula":formularioPelicula})