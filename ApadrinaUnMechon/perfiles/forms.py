from django import forms
from django.forms import widgets
from django.forms.fields import ChoiceField, TypedChoiceField
from django.forms.widgets import PasswordInput, Widget

tipo_alumno = [
    (0,'Padrino'),
    (1,'Mechon'),
    (2,'Moderador'),
    (3,'Super_padrino')
]

gustos_alumnos = [
    (0,'Videojuegos'),
    (1,'Programar'),
    (2,'Cocinar'),
    (3,'Musica'),
    (4,'Rol'),
    (5,'Peliculas / Series'),
    (6,'Puzzles'),
    (7,'Astronomia'),
    (8,'Debate'),
    (9,'Matematicas'),
]

class FormularioRegistro(forms.Form):

    rut = forms.CharField(label="Rut", required=True)
    nombre = forms.CharField(label="Nombre", required=True)
    usuario = forms.CharField(label="Usuario intranet",required=True)
    password = forms.CharField(label="Password", required=True, widget = PasswordInput)
    password2 = forms.CharField(label="Repetir Pasword",required=True, widget= PasswordInput)
    apellido_pat = forms.CharField(label="Apellido_pat", required=True)
    correo_ins = forms.EmailField(label="Correo_ins", required=True)
    correo_per = forms.EmailField(label="Correo_per", required=True)
    telefono = forms.CharField(label="Telefono", required=True)
    descripcion = forms.CharField(label="Descripcion", required=True)
    tipo = TypedChoiceField(label="Tipo", required=True, choices = tipo_alumno)
    gusto = TypedChoiceField(label="Gusto", required=True, choices= gustos_alumnos)


"""
class FormularioLogin(forms.Form):

    usuario = forms.CharField(label="Usuario",required=True)
    password = forms.CharField(label="Constrasena", required=True)
"""    