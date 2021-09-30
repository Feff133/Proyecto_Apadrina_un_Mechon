from django.db import models
from django.contrib.auth.models import User

# Create your models here.

category = [
    (0,'Consulta'),
    (1,'Informacion'),
    (2,'Informacion importante'),
    (3,'Aviso'),
]

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre

class Post(models.Model):
    Titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.Titulo

