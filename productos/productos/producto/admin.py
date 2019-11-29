from django.contrib import admin

from .models import Producto, Categoria


class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'descripcion', 'url_imagen', 'precio_unidad', 'categoria']
    list_filter = ['categoria']


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'categoria_padre']


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
