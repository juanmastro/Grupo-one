from django import forms

class UsuarioForm (forms.Form):

    nombre =  forms.CharField (max_length=40)
    apellido = forms.CharField(max_length=40)
    fechaNacimiento = forms.DateField()
    email = forms.EmailField()
    contrasena = forms.CharField(widget=forms.PasswordInput,max_length=40)


class PeliculaForm(forms.Form):

    nombre = forms.CharField (max_length=40)
    año = forms.IntegerField ()
    director = forms.CharField (max_length=40,)
    genero = forms.CharField (max_length=40)
    duracion = forms.TimeField()

class FormNewsletter(forms.Form):
    
    email = forms.EmailField()
