from django.shortcuts import redirect, render
from .forms import FormularioActividad
from actividades.models import Actividad
from perfiles.models import P_M, Persona_Auth

# Create your views here.

def actividades(request):
    #if not request.user.is_authenticated:
        #return render(request,'perfiles/login.html')

    act = Actividad.objects.all()

    return render(request, "actividades/actividades.html",{'actividades':act})

def agendar_actividad(request):

    formulario_actividad = FormularioActividad()

    if request.method == 'POST':

        formulario_actividad = FormularioActividad(data=request.POST)

        if formulario_actividad.is_valid():
            nom = request.POST.get("nombre")
            fecha_a = request.POST.get("fecha_actividad")
            hora_a = request.POST.get("hora_actividad")
            desc = request.POST.get("descripcion")

            usuario = Persona_Auth.objects.get(user=request.user)

            if usuario.tipo == 0:
                print(fecha_a)

                otro = P_M.objects.get(rut_p = usuario.rut, estado=1)
                
                a = Actividad(nombre = nom, descripcion = desc, estado=0, rut_p=usuario, rut_m = otro.rut_m, fecha_agendada = fecha_a, hora = hora_a)
                a.save()

                return redirect("/actividades/?valido")

            elif usuario.tipo == 1:

                otro = P_M.objects.get(rut_m = usuario.rut, estado=1)
                
                a = Actividad(nombre = nom, descripcion = desc, estado=0, rut_p=otro.rut_p, rut_m = usuario, fecha_agendada = fecha_a, hora = hora_a)
                a.save()

                return redirect("/actividades/?valido")


    return render(request,"actividades/agendar.html",{'formulario_actividad':formulario_actividad})