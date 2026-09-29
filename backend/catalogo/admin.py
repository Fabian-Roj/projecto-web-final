from django.contrib import admin
from .models import Servicio

# Register your models here.
@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "activo", "creado_en")
    list_filter = ("activo",)
    search_fields = ("nombre",)