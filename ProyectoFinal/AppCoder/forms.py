from django import forms

class UsuarioForm (forms.Form):

    nombre =  forms.CharField (max_length=40)
    edad = forms.IntegerField ()
    direccion =  forms.CharField (max_length=40)
    fechaNacimiento = forms.IntegerField()

