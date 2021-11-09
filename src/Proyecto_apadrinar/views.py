from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from django.views.generic.base import TemplateResponseMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from perfiles.models import Persona_Auth

# Create your views here.

#class HomePageView(LoginRequiredMixin, TemplateView):
 #   def get(self, request,**kwargs):
  #      return render(request,"index.html",context=None)






def inicio(request):

    return render(request, "Proyecto_apadrinar/inicio.html")

def archivos(request):

    return render(request, "Proyecto_apadrinar/archivos.html")



