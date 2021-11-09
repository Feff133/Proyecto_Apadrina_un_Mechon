from django import forms
from django.forms import widgets
from django.forms.fields import BooleanField, ChoiceField, TypedChoiceField
from django.forms.widgets import PasswordInput, Widget

tipo_alumno = [
    (0,'Padrino'),
    (1,'Mechon'),

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

carreras_u =[
    (0,'Geologia'),
    (1,'Ingenieria Civil'),
    (2,'Ingenieria Civil en Minas'),
    (3,'Ingenieria Civil Industrial'),
    (4,'Ingenieria Civil Informatica'),
    (5,'Ingenieria en Automatizacion y Robotica'),
    (6,'Ingenieria en Computacion e informatica'),
    (7,'Ingenieria en Costruccion'),
    (8,'Ingenieria en Marina Mercante'),
    (9,'Ingenieria Industrial'),

]

class FormularioRegistro(forms.Form):

    rut = forms.CharField(label="Rut ", required=True)
    nombre = forms.CharField(label="Nombre ", required=True)
    apellido_pat = forms.CharField(label="Apellido paterno ", required=True)
    usuario = forms.CharField(label="Usuario intranet ",required=True)
    password = forms.CharField(label="Password ", required=True, widget = PasswordInput)
    password2 = forms.CharField(label="Repetir Pasword ",required=True, widget= PasswordInput)
    carrera = TypedChoiceField(label="Carrera Universitaria ", required=True, choices= carreras_u)
    correo_ins = forms.EmailField(label="Correo institucional ", required=True)
    correo_per = forms.EmailField(label="Correo personal ", required=True)
    telefono = forms.CharField(label="Telefono ", required=True)
    descripcion = forms.CharField(label="Descripcion ", required=True,widget=forms.Textarea)
    #tipo = TypedChoiceField(label="Tipo ", required=True, choices = tipo_alumno)
    gusto = TypedChoiceField(label="Gusto ", required=True, choices= gustos_alumnos)
    ingreso = forms.BooleanField(label="Eres nuevo en la universidad?", required=False)



"""
class FormularioLogin(forms.Form):

    usuario = forms.CharField(label="Usuario",required=True)
    password = forms.CharField(label="Constrasena", required=True)
"""    