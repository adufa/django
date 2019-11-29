from django.db import models

# Create your models here.
class Residente(models.Model):

    id = models.AutoField(primary_key=True)

    nombre = models.CharField('Nombre', max_length=100)

    apellidos = models.CharField('Apellidos', max_length=100)

    fecha_nacimiento = models.DateField()

    def __str__(self):
        return '%s (%s) (%s)' % (self.id, self.nombre, self.fecha_nacimiento)

class Familiar(models.Model):

    id = models.AutoField(primary_key=True)

    nombre = models.CharField('Nombre', max_length=100)

    apellidos = models.CharField('Apellidos', max_length=100)

    parentesco = models.CharField('Parentesco', max_length=100)

    def __str__(self):
        return '%s (%s) (%s)' % (self.id, self.nombre, self.parentesco)

class Informe(models.Model):

    id = models.AutoField(primary_key=True)

    fecha_informe = models.DateField()

    def __str__(self):
        return '%s (%s)' % (self.id, self.fecha_informe)

class ParteInforme(models.Model):

    id = models.AutoField(primary_key=True)

    tipos = (
        ("SANTIARIA", "Santiaria"),
        ("FUNCIONAL", "Funcional"),
        ("PSIQUICA", "Psiquica"),
        ("SOCIAL", "Social"),
        ("TERAPIA", "Terapia"),
        ("OCUPACIONAL", "Ocupacional"),
    )

    tipo = models.CharField(max_length=12, choices=tipos,default="SANTIARIA")

    valoracion_inicial = models.CharField('Valoración Inicial', max_length=100)

    objetivos = models.CharField('Objetivos', max_length=100)

    informe = models.ForeignKey(Informe, on_delete=models.CASCADE)

    def __str__(self):
        return '%s (%s)' % (self.id, self.tipo)