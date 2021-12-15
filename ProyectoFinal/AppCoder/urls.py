from django.urls import path

from AppCoder import views

urlpatterns = [

    path("inicio/", views.inicio, name="Inicio"),
    path("madre/", views.madre, name="Madre"),
    path("registro/", views.formulario, name="Registro"),
    path("sobrenosotrxs/", views.sobreNosotrxs, name="Sobre nosotrxs"),
    path("post1/", views.post1, name="Post1"),
    path("contacto/", views.contacto, name="Contacto")
]
