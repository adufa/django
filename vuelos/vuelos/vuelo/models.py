from django.db import models


# Create your models here.
class Aeropuerto(models.Model):

    id = models.AutoField(primary_key=True)

    nombre = models.CharField(max_length=100)

    ciudad = models.CharField(max_length=100)

    siglas = models.CharField(max_length=25)

    def __str__(self):

            return self.nombre


class Vuelo(models.Model):

    id = models.AutoField(primary_key=True)

    aeropuerto_salida = models.ForeignKey(Aeropuerto, on_delete=models.CASCADE, related_name="+")

    fecha_salida = models.DateTimeField()

    aeropuerto_llegada = models.ForeignKey(Aeropuerto, on_delete=models.CASCADE)

    fecha_llegada = models.DateTimeField()

    codigo_vuelo = models.CharField(max_length=10)

    def __str__(self):

            return self.codigo_vuelo


class Cliente(models.Model):

    id = models.AutoField(primary_key=True)

    nombre = models.CharField(max_length=100)

    apellidos = models.CharField(max_length=100)

    email = models.EmailField(max_length=144)

    fecha_nacimiento = models.DateTimeField()

    def __str__(self):
        return '%s (%s)' % (self.nombre, self.apellidos)


class Reserva(models.Model):

    id = models.AutoField(primary_key=True)

    vuelo = models.ForeignKey(Vuelo, on_delete=models.CASCADE)

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    fecha_reserva = models.DateTimeField()

    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.id
