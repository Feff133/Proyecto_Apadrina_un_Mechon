from django.shortcuts import render

# Create your views here.

def archivos(request):

    return render(request, "archivos/archivos.html")