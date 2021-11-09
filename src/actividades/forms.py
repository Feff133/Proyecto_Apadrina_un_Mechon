from django import forms
from django.db.models.fields import DateTimeField
from django.forms import widgets
from django.forms.fields import BooleanField, ChoiceField, TypedChoiceField
from django.forms.forms import Form
from django.forms.widgets import DateInput, DateTimeInput, PasswordInput, SelectDateWidget, SplitDateTimeWidget, TimeInput, Widget


class FormularioActividad(forms.Form):
    nombre = forms.CharField(label="Actividad que se realizara ",required=True)
    fecha_actividad = forms.DateField(label="Dia (dd-mm-aa)",required=True)
    hora_actividad = forms.TimeField(label="Hora (Hora:Minutos)",required=True,widget=forms.TimeInput(format='%H:%M'))
    descripcion = forms.CharField(label="Descripcion ",required=True, widget=forms.Textarea)


