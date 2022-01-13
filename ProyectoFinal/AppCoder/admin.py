from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Usuario)
admin.site.register(Pelicula)
admin.site.register(Newsletter)
admin.site.register(Avatar)