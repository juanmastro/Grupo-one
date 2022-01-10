from django.urls import path
from AppCoder import views

urlpatterns = [

    path("inicio/", views.inicio, name="Inicio"),
    path("sobrenosotrxs/", views.sobreNosotrxs, name="Sobre nosotrxs"),
    path("post1/", views.post1, name="Post1"),
    path("contacto/", views.contacto, name="Contacto"),
    path("userFormulario/", views.userFormulario, name="UserFormulario"),
    path("proponerpeli/", views.proponerPeli, name="ProponerPeli"),
    path("newsletter/", views.Newsletter, name="Newsletter"),
    path("peliFormulario/", views.peliFormulario, name="PeliFormulario"),
    path("busquedapeli/", views.busquedapeli, name="Busquedapeli"),
    path("buscar/", views.buscar, name="Buscar"),
    path("resultadobusqueda/", views.resultadobusqueda, name="Resultadobusqueda"),
    path("leerpeliculas/", views.leerpeliculas, name="Leerpeliculas"),
    

    ]