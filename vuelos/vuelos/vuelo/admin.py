from django.contrib import admin
from .models import Aeropuerto, Cliente, Vuelo, Reserva
# Aeropuerto, Cliente, Vuelo y Reserva
# Register your models here.


class AeropuertoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'ciudad', 'siglas']
    list_filter = ['ciudad']


class VueloAdmin(admin.ModelAdmin):
    list_display = ['id', 'codigo_vuelo', 'aeropuerto_salida', 'aeropuerto_llegada', 'fecha_salida']
    list_filter = ['aeropuerto_salida', 'aeropuerto_llegada']


class ReservaAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'fecha_reserva', 'precio']
    list_filter = ['precio']


class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'apellidos', 'email']


admin.site.register(Aeropuerto, AeropuertoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Vuelo, VueloAdmin)
admin.site.register(Reserva, ReservaAdmin)