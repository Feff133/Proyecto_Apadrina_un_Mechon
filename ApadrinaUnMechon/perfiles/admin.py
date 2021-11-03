from django.contrib import admin
from .models import Persona_Auth, P_M

# Register your models here.
class Alumno_Admin(admin.ModelAdmin):
    list_display=("rut","user","correo_per","tipo","carrera")
    search_fields=("rut","tipo")
    list_filter=("tipo","carrera")

class P_M_Admin(admin.ModelAdmin):
    list_display=("codigo","rut_p","rut_m","estado","fecha_creada")
    search_fields=("codigo","rut_p","rut_m","estado","fecha_creada")
    list_filter=("estado","fecha_creada")

admin.site.register(Persona_Auth,Alumno_Admin)
admin.site.register(P_M,P_M_Admin)