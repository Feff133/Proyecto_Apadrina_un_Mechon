from django.db import models
from django.db.models.fields.files import FileField

# Create your models here.
estados = [
    (0,"activo"),
    (1,"quitado"),
]


class Archivo(models.Model):
    nombre = models.CharField(max_length=100)
    archivo = models.URLField(null=False, blank=False)
    descripcion = models.CharField(max_length=100)
    estado = models.IntegerField(choices=estados)