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


#LOGIN
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required





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

        userInsta = Usuario (nombre=request.POST["nombre"], apellido=request.POST["apellido"],fechaNacimiento = request.POST["fechaNacimiento"],correo=request.POST["correo"], contrasena=request.POST["contrasena"]  )  

        userInsta.save() #Guarda en la base de datos

        return render(request, "AppCoder/registrook.html")
    else:
        miFormulario = UsuarioForm()


    return render(request, 'AppCoder/userFormulario.html', {"miFormulario":miFormulario})


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



#LOGIN
def login_request(request):
    
    if request.method =="POST":
        
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            
            user = authenticate(username=usuario, password = contra)
            
            if user is not None:
                
                login(request, user)
                
                return render(request, "AppCoder/inicio.html", {"mensaje":f"BIENVENIDO, {usuario}!!!!"})
                
            else:
                
                return render(request, "AppCoder/inicio.html", {"mensaje":f"DATOS MALOS :(!!!!"})
                
            
        else:
            
            return render(request, "AppCoder/inicio.html", {"mensaje":f"FORMULARIO erroneo"})
            
            
    
    
    form = AuthenticationForm()  #Formulario sin nada para hacer el login
    
    return render(request, "AppCoder/login.html", {"form":form} )



def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            
            form = UserRegisterForm(request.POST)
            
            if form.is_valid():

                  username = form.cleaned_data['username']
                  
                  
                  form.save()
                  
                  return render(request,"AppCoder/inicio.html" ,  {"mensaje":f"{username} Creado :)"})


      else:
            #form = UserCreationForm()     
            
              
            form = UserRegisterForm()     

      return render(request,"AppCoder/register.html" ,  {"form":form})
  
  
  
  
@login_required
def editarPerfil(request):
    
    
    usuario = request.user
    
    if request.method == 'POST':
        
        miFormulario = UserEditForm(request.POST)
        
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data
            
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            
            usuario.save()
            
            return render(request, "AppCoder/inicio.html")
        
    else:
        
        miFormulario = UserEditForm(initial={'email':usuario.email})
        
        
    return render(request, "AppCoder/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})




@login_required
def agregarAvatar(request):
      if request.method == 'POST':

            miFormulario = AvatarFormulario(request.POST, request.FILES) #aquí mellega toda la información del html

            if miFormulario.is_valid():   #Si pasó la validación de Django


                  u = User.objects.get(username=request.user)
                
                  avatar = Avatar (user=u, imagen=miFormulario.cleaned_data['imagen']) 
      
                  avatar.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= AvatarFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/agregarAvatar.html", {"miFormulario":miFormulario})


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
