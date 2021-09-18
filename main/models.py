import datetime

from django.db import models
from django.contrib.auth.models import User
from datetime import date
from datetime import timedelta
from .choices import *

# Create your models here.
class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    link = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    codigo = models.CharField(max_length=4)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre

class Plato(models.Model):
    # Relaciones
    categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True)
    proveedor = models.ForeignKey('Proveedor', on_delete=models.SET_NULL, null=True)

    # Atributos
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField()
    receta = models.TextField()
    calorias = models.FloatField(null=True)
    ## Opciones de alimentación
    alimentacion = models.FloatField(choices=ALIMENTACION_CHOICES, null=True)

    # Metodos
    def sku(self):
        codigo_categoria = self.categoria.codigo.zfill(4)
        codigo_plato = str(self.id).zfill(6)
        return f'{codigo_categoria}-{codigo_plato}'
    def __str__(self):
        return self.nombre

class Profile(models.Model):
    # Relacion con el modelo User de Django
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Atributos adicionales para el usuario
    documento_identidad = models.CharField(max_length=8)
    edad = models.FloatField()
    talla = models.FloatField()
    peso = models.FloatField()
    ## Opciones de genero
    genero = models.CharField(max_length=2, choices=GENERO_CHOICES)
    ## Nivel de actividad
    nivelactividad = models.FloatField(choices=ACTIVO_CHOICES, null=True)
    ## Opciones de alimentación
    alimentacion = models.FloatField(choices=ALIMENTACION_CHOICES, null=True)
    objetivo = models.FloatField(choices=OBJETIVO_CHOICES, null=True)
    def metodotmb(self):
        calorias = 0
        if (self.genero == 'MA'):
            calorias = 66 + (13.7*self.peso) + (5*self.talla) - (6.75*self.edad)
        else:
            calorias = 655 + (9.6*self.peso) + (1.8*self.talla) - (4.7*self.edad)
        return calorias
    def caloriasdiarias(self):
        calorias = self.metodotmb()*self.nivelactividad
        return calorias
    def bajarpeso(self):
        return round(self.caloriasdiarias()-500)
    def mantenerpeso(self):
        return round(self.caloriasdiarias())
    def subirpeso(self):
        return round(self.caloriasdiarias()+500)
    def __str__(self):
        return self.user.get_username()


class Menu(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, null=True)
    fecha_creacion = models.DateField(auto_now=True)
    fecha_fin = models.DateField(blank=True, null=True)
    ## Opciones de alimentación
    VEGANO = 1
    VEGETARIANO = 2
    CARNE = 3
    alimentacion = models.IntegerField(choices=ALIMENTACION_CHOICES, null=True)
    estado = models.CharField(max_length=10, default='No Pagado')
    def precio(self):
        base = 30
        dias = self.fecha_fin - self.fecha_creacion
        meses = dias.days / 30
        if (meses<=1):
            return meses* base
        elif (meses>1 and meses<=6):
            return meses * base*0.8
        else:
            return meses * base*0.6
    def objetivo(self):
        return self.profile.objetivo
    def calcular_meses(self):
        meses = self.fecha_fin - self.fecha_creacion
        return meses.days
    def __str__(self):
        return f'Menú de {self.profile.user.get_username()} - {self.fecha_creacion}'

class DetalleMenu(models.Model):
    plato = models.ForeignKey('Plato', on_delete=models.CASCADE)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.plato.nombre} del {self.menu.__str__()}'

class PlatoImage(models.Model):
    plato = models.ForeignKey('Plato', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to="platos", null=True, blank=True)
