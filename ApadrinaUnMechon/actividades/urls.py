from django.urls import path

from . import views

urlpatterns = [
    path('',views.actividades, name="Actividades"),
    path('agendar/',views.agendar_actividad, name="agendar"),

]