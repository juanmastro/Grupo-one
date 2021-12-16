from django.shortcuts import render
from django.http import HttpResponse    
from datetime import datetime
from django.template import Template, Context
from django.template import loader

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import usuario, pelicula, serie
from AppCoder.forms import UsuarioForm



# Create your views here.

def madre(request):
    return render(request,"AppCoder/madre.html")

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
            userInsta = usuario (nombre=request.POST["nombre"], edad=request.POST["edad"],direccion = request.POST["direccion"],fechaNacimiento = request.POST["fechaNacimiento"] )  
            userInsta.save() #Guarda en la base de datos

        return render(request, "AppCoder/registrook.html")
    
    else:
        miFormulario = UsuarioForm()


    return render(request, 'AppCoder/userFormulario.html', {"miFormulario":miFormulario})

    