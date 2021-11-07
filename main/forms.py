from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class UserForm(UserCreationForm):
    # django.contrib.auth.User attributes
    first_name = forms.CharField(max_length=150, required=False)
    last_name = forms.CharField(max_length=150, required=False)
    email = forms.EmailField(max_length=150)

    # Atributos adicionales para el usuario
    documento_identidad = forms.CharField(max_length=8)
    edad = forms.FloatField()
    talla = forms.FloatField()
    peso = forms.FloatField()
    # Opciones de genero
    MASCULINO = 'MA'
    FEMENINO = 'FE'
    GENERO_CHOICES = [
        (MASCULINO, 'Masculino'),
        (FEMENINO, 'Femenino'),
    ]
    genero = forms.ChoiceField(choices=GENERO_CHOICES)
    # Nivel de actividad
    BAJAACTIVIDAD = 1.2
    MEDACTIVIDAD = 1.375
    ACTIVO = 1.55
    MUYACTIVO = 1.72
    ACTIVO_CHOICES = [
        (BAJAACTIVIDAD, 'No Muy Activo'),
        (MEDACTIVIDAD, 'Medianamente Activo'),
        (ACTIVO, 'Activo'),
        (MUYACTIVO, 'Muy Activo'),
    ]
    nivelactividad = forms.ChoiceField(choices=ACTIVO_CHOICES)
    # Opciones de alimentación
    VEGETARIANO = 2
    VEGANO = 1
    CARNE = 3
    ALIMENTACION_CHOICES = [
        (VEGETARIANO, 'Vegana'),
        (VEGANO, 'Vegetariana'),
        (CARNE, 'Carne')
    ]
    alimentacion = forms.ChoiceField(choices=ALIMENTACION_CHOICES)
    objetivo = forms.ChoiceField(choices=OBJETIVO_CHOICES)

    class Meta:
        model = User
        fields =  fields = ['username',
        'first_name',
        'last_name',
        'email',
        'documento_identidad',
        'edad',
        'talla',
        'genero',
        'peso',
        'nivelactividad',
        'alimentacion',
        'objetivo',
        ]
