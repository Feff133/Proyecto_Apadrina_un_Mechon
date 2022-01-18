from django.contrib import admin
from .models import Archivo

# Register your models here.

class Archivo_Admin(admin.ModelAdmin):
    list_display=("nombre","archivo","estado")
    search_fields=("nombre","estado")

admin.site.register(Archivo,Archivo_Admin)