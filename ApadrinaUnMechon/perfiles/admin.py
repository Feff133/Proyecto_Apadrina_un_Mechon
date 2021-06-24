from django.contrib import admin
from .models import Persona, P_M

# Register your models here.
class Alumno_Admin(admin.ModelAdmin):
    list_display=("rut","correo_ins","tipo")
    search_fields=("rut","tipo")
    list_filter=("tipo",)

admin.site.register(Persona,Alumno_Admin)
admin.site.register(P_M)