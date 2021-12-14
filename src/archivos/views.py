from django.shortcuts import redirect, render
from .forms import FormularioArchivos
from.models import Archivo

# Create your views here.

def archivos(request):
    arch = Archivo.objects.all()

    return render(request, "archivos/archivos.html",{'Archivos':arch})

def subir_archivo(request):
    formulario = FormularioArchivos()

    if request.method == "POST":
        formulario = FormularioArchivos(request.POST, request.FILES)
        if formulario.is_valid():
            archi = request.POST.get("archivo")
            desc = request.POST.get("descripcion")

            arch = Archivo(archivo = archi, descripcion = desc, estado = 0)
            arch.save()

            return redirect("Archivos")

    return render(request, "archivos/subida.html",{'formulario':formulario})