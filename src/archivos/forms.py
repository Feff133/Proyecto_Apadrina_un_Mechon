from django import forms
from django.forms.widgets import Textarea



class FormularioArchivos(forms.Form):
    nombre = forms.CharField(label="Nombre descripivo ")
    archivo = forms.URLField(label="Link del archivo ")
    descripcion = forms.CharField(label="Descripción ", widget= Textarea)


