from django.db import models
from django.db.models.fields import CharField, IntegerField
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

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

carreras_u =[
    (0,'Geologia'),
    (1,'Ingenieria Civil'),
    (2,'Ingenieria Civil en Minas'),
    (3,'Ingenieria Civil Industrial'),
    (4,'Ingenieria Civil Informatica'),
    (5,'Ingenieria en Automatizacion y Robotica'),
    (6,'Ingenieria en Computacion e informatica'),
    (7,'Ingenieria en Costruccion'),
    (8,'Ingenieria en Marina Mercante'),
    (9,'Ingenieria Industrial'),

]

state = [
    (0,"pendiente"),
    (1,"activo"),
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
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    correo_per = models.EmailField(blank=True, null=True, verbose_name='Correo Personal')
    telefono = models.CharField(max_length=12, blank=True, null=True)
    descripcion = models.CharField(max_length=300,null=False,blank=False)
    tipo = models.IntegerField(choices = tipo_alumno)
    gusto = models.IntegerField(choices = gustos_alumnos, null= True)
    carrera = models.IntegerField(choices= carreras_u ,null=False, blank=False)
 
    def __str__(self):
        return str(self.rut)

class P_M(models.Model):
    codigo = models.AutoField(primary_key=True,null=False,blank=False,unique=True)
    rut_p = models.ForeignKey('Persona_Auth', related_name='alumno_padrino', on_delete=models.CASCADE)
    rut_m = models.ForeignKey('Persona_Auth', related_name='alumno_mechon', on_delete=models.CASCADE)
    estado = models.IntegerField(choices=state, null=False, blank=False)
    fecha_creada = models.DateField(auto_now=True)

#@receiver(post_save, sender=User)
#def create_user_profile(sender, instance,created,**kwargs):
 #   if created:
  #      Persona_Auth.objects.create(User=instance)


