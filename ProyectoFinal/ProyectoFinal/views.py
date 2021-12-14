from django.http import HttpResponse    
from datetime import datetime
from django.template import Template, Context

def saludo (request):
    return HttpResponse ("Hola Django - Coder")

def segundaVista (request):
    return HttpResponse ("Hola loke/ ya soy un programador brillante")

def dia (request):
    variable = datetime.now () 
    return HttpResponse (f"Hoy es un gran dia {variable}")

def probandoTemplate (seft):
    mihtml = open ()
    pantilla = Template (mihtml.read())
    
    mihtml.close()

    miContexto = Context ()
    documento = pantilla.render (miContexto)

    return HttpResponse (documento)