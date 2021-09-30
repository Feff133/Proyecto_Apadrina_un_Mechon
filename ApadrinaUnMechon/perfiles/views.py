from django.shortcuts import render, redirect
from perfiles.models import Persona_Auth
from .forms import FormularioRegistro
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse


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

# def login(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect(request, "perfiles/perfiles.html")
        else:
            messages.info(request,'credenciales invalidas')
            return redirect(request, "perfiles/login.html")

    return render(request, "perfiles/login.html")


def perfiles(request):
    
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
            Ap_pat = request.POST.get("apellido_pat")
            C_ins = request.POST.get("correo_ins")
            C_per = request.POST.get("coreo_per")
            Tel = request.POST.get("telefono")
            Desc = request.POST.get("descripcion")
            Type = request.POST.get("tipo")
            Gust = request.POST.get("gusto")

            #p = Persona_Auth(rut = Rut, nombre = Nom, password = Pass, apellido_pat = Ap_pat, apellido_mat = Ap_mat, correo_ins = C_ins, correo_per = C_per, telefono = Tel, descripcion = Desc, tipo = Tipo, gusto = Gusto)
            c_user = User.objects.create_user(username = usuario, email = C_ins, password = Pass, first_name = Nom, last_name = Ap_pat)
        

            """for x in usuarios:
                if x.username == usuario:
                    n_usuario = x.username
                    return n_usuario
"""

            p = Persona_Auth(rut = Rut, user = c_user , correo_per = C_per, telefono = Tel, descripcion = Desc, tipo = Type, gusto = Gust)
            p.save()

            return redirect("/perfiles/?valido")


    return render(request, "perfiles/registro.html",{'miFormulario':formulario_registro})