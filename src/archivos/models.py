from django.db import models
from django.db.models.fields.files import FileField

# Create your models here.
estados = [
    (0,"activo"),
    (1,"bajado"),
]


class Archivo(models.Model):
    archivo = models.FileField(upload_to='archivos_subidos/')
    descripcion = models.CharField(max_length=100)
    estado = models.IntegerField(choices=estados)