from django import forms
from django.forms.widgets import Textarea



class FormularioArchivos(forms.Form):
    archivo = forms.FileField()
    descripcion = forms.CharField(label="Descripción ", widget= Textarea)


