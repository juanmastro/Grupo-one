from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path("inicio/", views.inicio, name="Inicio"),
    path("sobrenosotrxs/", views.sobreNosotrxs, name="Sobre nosotrxs"),
    path("post1/", views.post1, name="Post1"),
    path("contacto/", views.contacto, name="Contacto"),
    path("userFormulario/", views.userFormulario, name="userFormulario"),
    path("proponerpeli/", views.proponerPeli, name="ProponerPeli"),
    path("newsletter/", views.Newsletter, name="Newsletter"),
    path("peliFormulario/", views.peliFormulario, name="peliFormulario"),
    path('login', views.login_request, name="Login"),
    path('register', views.register, name="Register"),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name="Logout"),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    path('agregarAvatar', views.agregarAvatar, name="AgregarAvatar"),

]