from django.contrib import admin
from .models import Residente, Familiar, Informe, ParteInforme

# Register your models here.
class ResidenteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'apellidos', 'fecha_nacimiento']
    list_filter = ['nombre']

class FamiliarAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'apellidos', 'parentesco']
    list_filter = ['nombre']

class InformeAdmin(admin.ModelAdmin):
    list_display = ['id', 'fecha_informe']
    list_filter = ['id']

class ParteInformeAdmin(admin.ModelAdmin):
    list_display = ['id', 'tipo', 'valoracion_inicial', 'objetivos']
    list_filter = ['id']

admin.site.register(Residente, ResidenteAdmin)
admin.site.register(Familiar, FamiliarAdmin)
admin.site.register(Informe, InformeAdmin)
admin.site.register(ParteInforme, ParteInformeAdmin)
