from django.shortcuts import render, redirect
from perfiles.models import Persona_Auth, P_M
from .forms import FormularioRegistro
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.conf import settings
from django.core.files import File


# Create your views here.


def login_view(request):

    if request.user.is_authenticated:

        return HttpResponseRedirect(reverse('Perfiles')) 

    context = {}

    template_name = 'perfiles/login.html'

    if request.POST:

        username = request.POST['username']

        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request,user)

            return HttpResponseRedirect(reverse('Perfiles'))

        else:

            context['error'] = "Usuario o contraseña incorrecta"

    return render(request, template_name, context)

def logout_view(request):

    context = {}

    template_name = 'perfiles/login.html'

    logout(request)

    return render(request, template_name, context)



def vincular(request):
    if request.POST:
        apadrinado =Persona_Auth(pk=request.POST['dato'])
        current_u = request.user
        usuario = Persona_Auth.objects.get(user=request.user)
        if usuario.tipo == 0:
            relacion = P_M(rut_p=usuario, rut_m=apadrinado, estado=0,sender=current_u.username)
            relacion.save()
        elif usuario.tipo == 1:
            relacion = P_M(rut_p=apadrinado, rut_m=usuario, estado=0,sender=current_u.username)
            relacion.save()

    return redirect("Perfiles")

def perfiles(request):
    if not request.user.is_authenticated:
        return render(request,'perfiles/login.html')

    usuarios = User.objects.all()
    personas = Persona_Auth.objects.all()

    return render(request, "perfiles/perfiles.html", {"personas": personas, "usuarios":usuarios})

def registro(request):

    formulario_registro = FormularioRegistro()

    if request.method == "POST":
        formulario_registro = FormularioRegistro(data=request.POST)

        if formulario_registro.is_valid():

            Rut = request.POST.get("rut")
            Nom = request.POST.get("nombre")
            usuario = request.POST.get("usuario")
            Pass = request.POST.get("password")
            Pass2 = request.POST.get("password2")
            Ap_pat = request.POST.get("apellido_pat")
            Carr = request.POST.get("carrera")
            C_ins = request.POST.get("correo_ins")
            C_per = request.POST.get("correo_per")
            Tel = request.POST.get("telefono")
            Desc = request.POST.get("descripcion")
            ingreso = request.POST.get("ingreso")
            Gust = request.POST.get("gusto")
            #Gust2 = request.POST.get("interes")
            

            if Pass == Pass2:
                #casilla activada
                if ingreso == "on":
                    tipo_u = 1
                    c_user = User(username = usuario, email = C_ins, password = Pass, first_name = Nom, last_name = Ap_pat)
                    c_user.set_password(Pass)
                    c_user.save()
                    p = Persona_Auth(rut = Rut, user = c_user , correo_per = C_per, telefono = Tel, descripcion = Desc, tipo = tipo_u, gusto = Gust, carrera = Carr)
                    p.save()
                #casilla desactivada
                elif ingreso == None:
                    tipo_u = 0
                    c_user = User(username = usuario, email = C_ins, password = Pass, first_name = Nom, last_name = Ap_pat)
                    c_user.set_password(Pass)
                    c_user.save()
                    p = Persona_Auth(rut = Rut, user = c_user , correo_per = C_per, telefono = Tel, descripcion = Desc, tipo = tipo_u, gusto = Gust, carrera = Carr)
                    p.save()

                return redirect("/perfiles/login/?valido")

            else:
                messages.info(request,"Contrasenas no coinciden")
                return redirect("registro")

    return render(request, "perfiles/registro.html",{'miFormulario':formulario_registro})


def solicitudes(request):
    if not request.user.is_authenticated:
        return render(request,'perfiles/login.html')

    current_u = Persona_Auth.objects.get(user=request.user) 

    if current_u.tipo == 0:
        solici = P_M.objects.filter(rut_p=current_u.rut)
        return render(request, "perfiles/solicitudes.html",{'solicitudes':solici})
    elif current_u.tipo == 1:
        solici = P_M.objects.filter(rut_m=current_u.rut)
        return render(request, "perfiles/solicitudes.html",{'solicitudes':solici})



def aceptar(request):

    if request.POST:
        rut_per =P_M.objects.get(codigo=request.POST['dato'])
        rut_per.estado = 1
        rut_per.save()

    return redirect("solicitudes")

def load_data(request):
    usuarios = [
        {
            'first_name': 'Felipe',
            'last_name':'Fuentes',
            'username':'f.fuentesbaez',
            'password':'7481025fF',
            'email':'f.fuentesbaez@uandresbello.edu',
            'datos':{
                'rut': '20.428.832-1',          
                'correo_per':'felipefuentesbaez@gmail.com',
                'telefono':987654321,
                'descripcion':'Descripcion generica',
                'tipo':0,
                'gusto':0,
                'carrera':6,
            }

        },
        {
            'first_name': 'Barbara',
            'last_name':'Fuentes',
            'username':'b.fuentesbaez2',
            'password':'apadrina1234',
            'email':'b.fuentesbaez@uandresbello.edu',
            'datos':{
                'rut': '19.309.612-3',          
                'correo_per':'barbfuentesb@gmail.com',
                'telefono':987654321,
                'descripcion':'Descripcion generica',
                'tipo':1,
                'gusto':0,
                'carrera':0,
            }

        },
        {
            'first_name': 'Miguel',
            'last_name':'Canales',
            'username':'m.canalesaguilera',
            'password':'apadrina1234',
            'email':'m.canalesaguilera@uandresbello.edu',
            'datos':{
                'rut': '19.456.890-1',          
                'correo_per':'mctrachos@gmail.com',
                'telefono':987654321,
                'descripcion':'Descripcion generica',
                'tipo':0,
                'gusto':0,
                'carrera':0,
            }

        },
        {
            'first_name': 'Manuel',
            'last_name':'Fuentes',
            'username':'m.fuentestorres',
            'password':'apadrina1234',
            'email':'m.fuentestorres@uandresbello.edu',
            'datos':{
                'rut': '3.437.616-0',          
                'correo_per':'manuel.fuentes.t@gmail.com',
                'telefono':987654321,
                'descripcion':'Descripcion generica',
                'tipo':1,
                'gusto':0,
                'carrera':0,
            }

        },
        {
            'first_name': 'Nicolas',
            'last_name':'Roca',
            'username':'n.rocasanhueza',
            'password':'apadrina1234',
            'email':'n.rocasanhueza@uandresbello.edu',
            'datos':{
                'rut': '20.204.184-1',          
                'correo_per':'manuel.fuentes.t@gmail.com',
                'telefono':987654321,
                'descripcion':'Descripcion generica',
                'tipo':1,
                'gusto':0,
                'carrera':6,
            }

        },
    ]

    for x in usuarios:
        c_user = User.objects.create_user(username = x['username'], email = x['email'], password = x['password'], first_name = x['first_name'], last_name = x['last_name'])

        p = Persona_Auth.objects.create(rut = x['datos']['rut'], user = c_user , correo_per = x['datos']['correo_per'], telefono = x['datos']['telefono'], descripcion = x['datos']['descripcion'], tipo = x['datos']['tipo'], gusto = x['datos']['gusto'], carrera = x['datos']['carrera'])
        p.save()

    return redirect('login')