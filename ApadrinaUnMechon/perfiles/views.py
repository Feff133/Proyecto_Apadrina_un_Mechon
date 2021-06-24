from django.shortcuts import render
from perfiles.models import Persona

# Create your views here.

def perfiles(request):
    
    personas = Persona.objects.all()
    
    return render(request, "perfiles/perfiles.html", {"personas": personas})