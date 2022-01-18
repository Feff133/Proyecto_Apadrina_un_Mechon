from django.urls import path

from . import views

urlpatterns = [
    path('',views.archivos, name="Archivos"),
    path('subida/',views.subir_archivo,name="Subir_archivo"),
    path('borrar/',views.borrar_a,name="borrar"),
    


]