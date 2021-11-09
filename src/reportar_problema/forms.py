from django import forms

class FormularioProblema(forms.Form):

    nombre = forms.CharField(label="Nombre",required=True)
    email = forms.CharField(label="Email",required=True)
    problema = forms.CharField(label="Problema",required=True)
    contenido = forms.CharField(label="Contenido", widget=forms.Textarea)

