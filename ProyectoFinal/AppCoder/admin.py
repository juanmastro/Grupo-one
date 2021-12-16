from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(usuario)
admin.site.register(pelicula)
admin.site.register(serie)
