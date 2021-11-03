from django.contrib import admin
from .models import Actividad

# Register your models here.
class Actividad_Admin(admin.ModelAdmin):
    list_diplay = ("id","nombre","estado","rut_p","rut_m","fecha_agendada","hora","fecha_creada","updated")
    search_fields = ("nombre","estado","rut_p","rut_m","fecha_agendada","fecha_creada")
    list_filter = ("estado","fecha_agendada","fecha_creada")

admin.site.register(Actividad,Actividad_Admin)