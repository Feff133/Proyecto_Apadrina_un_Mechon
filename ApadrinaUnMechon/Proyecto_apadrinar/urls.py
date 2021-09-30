from django.urls import path

from Proyecto_apadrinar import views

urlpatterns = [
    path('',views.inicio, name="Inicio"),
    path('archivos',views.archivos, name="Descargas"),
    path('actividades',views.actividades, name="Actividades"),

]