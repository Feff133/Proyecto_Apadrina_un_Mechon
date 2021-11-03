from django.db import models
from perfiles.models import Persona_Auth

# Create your models here.

estados = [
    (0,"Activa"),
    (1,"Realizada"),
    (2,"Cancelada"),
    ]

class Actividad(models.Model):
    id = models.AutoField(primary_key=True,null=False,blank=False,unique=True)
    nombre = models.CharField(max_length=100,blank=True)
    descripcion = models.CharField(max_length=300,null=False,blank=False)
    estado = models.IntegerField(choices=estados, null=False)
    rut_p = models.ForeignKey('perfiles.Persona_Auth', related_name='alumno_pad', on_delete=models.CASCADE)
    rut_m = models.ForeignKey('perfiles.Persona_Auth', related_name='alumno_mec', on_delete=models.CASCADE)
    fecha_creada = models.DateTimeField(auto_now_add=True)
    fecha_agendada = models.DateField(blank=False)
    hora = models.TimeField(blank=False)
    updated = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return str(self.id)
