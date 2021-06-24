from django.urls import path

from . import views

urlpatterns = [
    path('',views.perfiles, name="Perfiles"),
]