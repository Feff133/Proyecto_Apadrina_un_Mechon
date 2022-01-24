from django.shortcuts import redirect, render
from .forms import FormularioArchivos
from.models import Archivo

# Create your views here.

def archivos(request):
    arch = Archivo.objects.filter(estado = 0)
    

    return render(request, "archivos/archivos.html",{'Archivos':arch})

def borrar_a(request):
    if request.POST:
        arch = Archivo.objects.get(id = request.POST['dato'])
        arch.estado = 1
        arch.save()
    
    return redirect("/archivos/?borrado")

def modificar_a(request):
    if request.POST:
        arc = Archivo.objects.get(id = request.POST['dato'])
        nomb_a = request.POST['nombre_a']
        lin_a = request.POST['link_a']
        des_a = request.POST['desc_a']
        current_u = request.user

        arc.nombre = nomb_a
        arc.archivo = lin_a
        arc.descripcion = des_a
        arc.subido_por = current_u

        arc.save()

        return redirect("/archivos/?modificado")

def subir_archivo(request):
    formulario = FormularioArchivos()

    if request.method == "POST":
        formulario = FormularioArchivos(request.POST)
        if formulario.is_valid():
            nomb = request.POST.get("nombre")
            archi = request.POST.get("archivo")
            desc = request.POST.get("descripcion")

            arch = Archivo(nombre = nomb, archivo = archi, descripcion = desc, estado = 0)
            arch.save()

            return redirect("/archivos/?subido")

    return render(request, "archivos/subida.html",{'formulario':formulario})