from django.contrib import admin
from .models import Persona_Auth, P_M

# Register your models here.
class Alumno_Admin(admin.ModelAdmin):
    list_display=("rut","correo_per","tipo")
    search_fields=("rut","tipo")
    list_filter=("tipo",)

admin.site.register(Persona_Auth,Alumno_Admin)
admin.site.register(P_M)