from django import forms

class UsuarioForm (forms.Form):

    nombre =  forms.CharField (required=True)
    edad = forms.IntegerField ()
    direccion =  forms.CharField ()
    fechaNacimiento = forms.IntegerField()
