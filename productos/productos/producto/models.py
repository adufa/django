from django.db import models


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=200)
    categoria_padre = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                                        related_name='categoria')

    def __str__(self):
        """
        String para representar el Objeto del Modelo
        """
        return '%s %s' % (self.id, self.nombre)


class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=250)
    url_imagen = models.CharField(max_length=250)
    precio_unidad = models.DecimalField(decimal_places=2, max_digits=10)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=False)

    def __str__(self):
        """
        String para representar el Objeto del Modelo
        """
        return '%s %s %s %s %s' % (self.id, self.nombre, self.descripcion, str(self.precio_unidad), self.categoria.nombre)
