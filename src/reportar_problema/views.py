from django.shortcuts import redirect, render

from .forms import FormularioProblema
from django.core.mail import EmailMessage

# Create your views here.

def problemas(request):
    if not request.user.is_authenticated:
        return render(request,'perfiles/login.html')

    formulario_problema = FormularioProblema()

    if request.method == "POST":
        formulario_problema = FormularioProblema(data=request.POST)

        if formulario_problema.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            problema = request.POST.get("problema")
            contenido = request.POST.get("contenido")

            email = EmailMessage("Nuevo problema de usuario en Apadrina un Mechon",
            "El usuario con nombre {} con el correo {} tiene un problema de tipo: {}\nEsto es lo que dice:\n\n {}".format(nombre, email, problema, contenido),
            "",["apadrinamechon@gmail.com"],reply_to=[email])

      
            email.send()

            return redirect("/reportar_problema/?valido")



    return render(request, "reportar_problema/problemas.html", {'miFormulario':formulario_problema})

