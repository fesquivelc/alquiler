# coding=utf-8
from django.db import models

# Create your models here.
class Institucion(models.Model):
    nombre = models.CharField(max_length=70)

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ('nombre',)
        verbose_name_plural = 'Instituciones'

class Departamento(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre

class Provincia(models.Model):
    departamento = models.ForeignKey(Departamento)
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return 'DEPT: %s PROV: %s' % (self.departamento, self.nombre)

    class Meta:
        ordering = ('departamento','nombre')

class Inquilino(models.Model):
    dni = models.CharField(max_length=8,primary_key=True)
    apellidopaterno = models.CharField(max_length=200, verbose_name='Apellido Paterno')
    apellidomaterno = models.CharField(max_length=200, verbose_name='Apellido Materno')
    nombres = models.CharField(max_length=200)
    institucion = models.ForeignKey(Institucion, null=True)
    provincia = models.ForeignKey(Provincia)
    telefono = models.CharField(max_length=9, null=True)
    celular = models.CharField(max_length=9)

    def __unicode__(self):
        return '%s %s, %s' % (self.apellidopaterno, self.apellidomaterno, self.nombres)

    class Meta:
        ordering = ('apellidopaterno','apellidomaterno','nombres')

class Cuarto(models.Model):
    numero = models.CharField(max_length=2, primary_key=True)
    costo = models.DecimalField(max_digits=5, decimal_places=2, default=80)
    descripcion = models.TextField(verbose_name='Descripción',max_length=500)

    def __unicode__(self):
        return 'CUARTO: %s - COSTO: %g' % (self.numero, self.costo)

class Alquiler(models.Model):
    cuarto = models.ForeignKey(Cuarto)
    inquilino = models.ForeignKey(Inquilino)
    fechainicio = models.DateField(auto_now=True, verbose_name='Fecha de inicio')
    fechafin = models.DateField(verbose_name='Fecha de fin')
