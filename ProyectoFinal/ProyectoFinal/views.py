from django.http import HttpResponse    
from datetime import datetime
from django.template import Template, Context

def saludo (request):
    return HttpResponse ("Bienvenido a la WEB Pelis-Pro-Play")

def templateUno (seft):

    fecha = datetime.now ()
    diccionario = {"fechaActualizada": fecha}

    mihtml = open ("C:\\Users\\u900768\\Desktop\\Proyecto\\Grupo-one\\ProyectoFinal\\ProyectoFinal\\plantillas\\template1.html")
    pantilla = Template (mihtml.read())
    
    mihtml.close()

    miContexto = Context (diccionario)
    documento = pantilla.render (miContexto)

    return HttpResponse (documento)