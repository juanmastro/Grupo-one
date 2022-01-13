from django import forms
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UsuarioForm (forms.Form):

    nombre =  forms.CharField (max_length=40)
    apellido = forms.CharField(max_length=40)
    fechaNacimiento = forms.DateField(required=False)
    correo = forms.EmailField(required=False)
    contrasena = forms.CharField(widget=forms.PasswordInput,max_length=40)
    


class PeliculaForm(forms.Form):

    nombre = forms.CharField (max_length=40)
    año = forms.IntegerField ()
    director = forms.CharField (max_length=40,)
    genero = forms.CharField (max_length=40)
    duracion = forms.TimeField()

class FormNewsletter(forms.Form):
    
    email = forms.EmailField()



class UserEditForm(UserCreationForm):

    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña')
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 
    #imagen_avatar = forms.ImageField(required=False)
  
class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)