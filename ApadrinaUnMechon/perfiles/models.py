from django.db import models
from django.db.models.fields import CharField, IntegerField
from django.contrib.auth.models import User

# Create your models here.

tipo_alumno = [
    (0,'Padrino'),
    (1,'Mechon'),
    (2,'Moderador'),
    (3,'Super_padrino')
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

"""
class Persona(models.Model):
    rut = models.CharField(max_length=12, primary_key=True, null=False, blank=False, unique=True)
    nombre = models.CharField(max_length=20)
    password = models.CharField(max_length=20, null=False, blank=False)
    apellido_pat = models.CharField(max_length=20)
    apellido_mat = models.CharField(max_length=20)
    correo_ins = models.EmailField(verbose_name='Correo Institucional')
    correo_per = models.EmailField(blank=True, null=True, verbose_name='Correo Personal')
    telefono = models.CharField(max_length=12, blank=True, null=True)
    descripcion = models.CharField(max_length=300,null=False,blank=False)
    tipo = models.IntegerField(choices = tipo_alumno)
    gusto = models.IntegerField(choices = gustos_alumnos, null= True)

    def __str__(self):
        return str(self.rut)
"""
class Persona_Auth(models.Model):
    rut = models.CharField(max_length=12, primary_key=True, null=False, blank=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    correo_per = models.EmailField(blank=True, null=True, verbose_name='Correo Personal')
    telefono = models.CharField(max_length=12, blank=True, null=True)
    descripcion = models.CharField(max_length=300,null=False,blank=False)
    tipo = models.IntegerField(choices = tipo_alumno)
    gusto = models.IntegerField(choices = gustos_alumnos, null= True)

    def __str__(self):
        return str(self.rut)

class P_M(models.Model):
    rut_p = models.ForeignKey('Persona_Auth', related_name='alumno_padrino', on_delete=models.CASCADE)
    rut_m = models.ForeignKey('Persona_Auth', related_name='alumno_mechon', on_delete=models.CASCADE)

