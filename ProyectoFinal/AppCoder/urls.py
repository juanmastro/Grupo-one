from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path("", views.inicio, name="Inicio"),
    path("sobrenosotrxs/", views.sobreNosotrxs, name="Sobre nosotrxs"),
    path("post1/", views.post1, name="Post1"),
    path("post2/", views.post2, name="Post2"),
    path("post3/", views.post3, name="Post3"),
    path("contacto/", views.contacto, name="Contacto"),
    path("userFormulario/", views.userFormulario, name="UserFormulario"),
    path("newsletter/", views.Newsletter, name="Newsletter"),
    path("proponerPeli/", views.proponerPeli, name="ProponerPeli"),

    path('login', views.login_request, name="Login"),
    path('register', views.register, name="Register"),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name="Logout"),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    path('agregarAvatar', views.agregarAvatar, name="AgregarAvatar"),

    path("peliFormulario/", views.peliFormulario, name="PeliFormulario"),
    path("busquedapeli/", views.busquedapeli, name="Busquedapeli"),
    path("buscar/", views.buscar, name="Buscar"),
    path("resultadobusqueda/", views.resultadobusqueda, name="Resultadobusqueda"),
    path("leerpeliculas/", views.leerpeliculas, name="Leerpeliculas"),
    

]
