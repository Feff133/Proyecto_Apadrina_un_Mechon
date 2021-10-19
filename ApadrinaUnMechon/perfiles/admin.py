from django.contrib import admin
from .models import Persona_Auth, P_M

# Register your models here.
class Alumno_Admin(admin.ModelAdmin):
    list_display=("rut","user","correo_per","tipo","carrera")
    search_fields=("rut","tipo")
    list_filter=("tipo","carrera")

admin.site.register(Persona_Auth,Alumno_Admin)
admin.site.register(P_M)