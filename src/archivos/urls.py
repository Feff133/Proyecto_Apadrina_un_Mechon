from django.urls import path

from . import views

urlpatterns = [
    path('',views.archivos, name="Archivos"),


]