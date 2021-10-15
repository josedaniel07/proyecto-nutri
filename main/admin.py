from django.contrib import admin
from .models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user",  "nombre", "apellido","documento_identidad",)

class MenuAdmin(admin.ModelAdmin):
    list_display = ("profile", "fecha_creacion", "fecha_fin", "estado", "precio", "dias_restantes")
    list_filter = ("fecha_creacion", )

class PlatosAdmin(admin.ModelAdmin):
    list_display = ("nombre", "calorias", "alimentacion", "categoria")
    list_filter = ("alimentacion", "categoria")


# Register your models here.
admin.site.register(Plato, PlatosAdmin)
admin.site.register(Categoria)
admin.site.register(Proveedor)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(DetalleMenu)