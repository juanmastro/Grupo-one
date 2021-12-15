from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def madre(request):
    return render(request,"AppCoder/madre.html")

def inicio(request):
    #return HttpResponse("Hola.")
    return render(request, "AppCoder/inicio.html")

def formulario(request,):
    return render(request,"AppCoder/formulario.html")

def sobreNosotrxs(request):
    return render(request, "AppCoder/sobrenosotrxs.html")

def post1(request):
    return render(request, "AppCoder/post1.html")

def usuario(request):
    return render(request)

def contacto(request):
    return render(request, "AppCoder/contacto.html")
