VEGETARIANO = 2
VEGANO = 1
CARNE = 3
ALIMENTACION_CHOICES = [
    (VEGETARIANO, 'Vegana'),
    (VEGANO, 'Vegetariana'),
    (CARNE, 'Carne')
]

BAJAACTIVIDAD = 1.2
MEDACTIVIDAD = 1.375
ACTIVO = 1.55
MUYACTIVO = 1.72
ACTIVO_CHOICES = [
    (BAJAACTIVIDAD, 'No Muy Activo'),
    (MEDACTIVIDAD, 'Medianamente Activo'),
    (ACTIVO, 'Activo'),
    (MUYACTIVO, 'Muy Activo')
]

MASCULINO = 'MA'
FEMENINO = 'FE'
GENERO_CHOICES = [
    (MASCULINO, 'Masculino'),
    (FEMENINO, 'Femenino')
]

bajar = -500
mantener = 0
subir = 500
OBJETIVO_CHOICES = [
    (bajar, 'Bajar de peso'),
    (mantener, 'Mantener tu peso'),
    (subir, 'Subir de peso')
]