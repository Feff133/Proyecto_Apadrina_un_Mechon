from django.shortcuts import render, HttpResponse

from perfiles.models import Persona

# Create your views here.

def login(request):

    return render(request, "Proyecto_apadrinar/login.html")


def blog(request):

    return render(request, "Proyecto_apadrinar/blog.html")

def inicio(request):

    return render(request, "Proyecto_apadrinar/inicio.html")

def archivos(request):

    return render(request, "Proyecto_apadrinar/archivos.html")

def actividades(request):

    return render(request, "Proyecto_apadrinar/actividades.html")

def problemas(request):

    return render(request, "Proyecto_apadrinar/problemas.html")