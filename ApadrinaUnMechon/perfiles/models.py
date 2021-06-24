from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.

tipo_alumno = [
    (0,'Padrino'),
    (1,'Mechon'),
    (2,'Moderador'),
    (3,'Super_padrino')
]

class Persona(models.Model):
    rut = models.IntegerField(primary_key=True, null=False, blank=False, unique=True)
    nombre = models.CharField(max_length=20)
    password = models.CharField(max_length=20, null=False, blank=False)
    apellido_pat = models.CharField(max_length=20)
    apellido_mat = models.CharField(max_length=20)
    correo_ins = models.EmailField(verbose_name='Correo Institucional')
    correo_per = models.EmailField(blank=True, null=True, verbose_name='Correo Personal')
    telefono = models.CharField(max_length=12, blank=True, null=True)
    descripcion = models.CharField(max_length=300,null=False,blank=False)
    tipo = models.IntegerField(choices = tipo_alumno)

    def __str__(self):
        return str(self.rut)

class P_M(models.Model):
    rut_p = models.ForeignKey('Persona', related_name='alumno_padrino', on_delete=models.CASCADE)
    rut_m = models.ForeignKey('Persona', related_name='alumno_mechon', on_delete=models.CASCADE)

