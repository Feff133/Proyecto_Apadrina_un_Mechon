from django.urls import path

from Proyecto_apadrinar import views

urlpatterns = [
    path('',views.login, name="Login"),
    path('blog',views.blog, name="Blog"),
    path('inicio',views.inicio, name="Inicio"),
    path('archivos',views.archivos, name="Descargas"),
    path('actividades',views.actividades, name="Actividades"),
    path('problemas',views.problemas, name="Problemas"),
]