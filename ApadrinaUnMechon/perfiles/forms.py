from django import forms

class FormularioRegistro(forms.Form):

    rut = forms.CharField(label="Rut", required=True)
    nombre = forms.CharField(label="Nombre", required=True)
    usuario = forms.CharField(label="Usuario intranet",required=True)
    password = forms.CharField(label="Password", required=True)
    apellido_pat = forms.CharField(label="Apellido_pat", required=True)
    correo_ins = forms.EmailField(label="Correo_ins", required=True)
    correo_per = forms.EmailField(label="Correo_per", required=True)
    telefono = forms.CharField(label="Telefono", required=True)
    descripcion = forms.CharField(label="Descripcion", required=True)
    tipo = forms.IntegerField(label="tipo", required=True)
    gusto = forms.IntegerField(label="gusto", required=True)


"""
class FormularioLogin(forms.Form):

    usuario = forms.CharField(label="Usuario",required=True)
    password = forms.CharField(label="Constrasena", required=True)
"""    