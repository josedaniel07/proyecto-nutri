from django.contrib import admin
from .models import *

class PlatoImageInline(admin.TabularInline):
    model=PlatoImage


class PlatoAdmin(admin.ModelAdmin):
    inlines = [
        PlatoImageInline,
    ]
# Register your models here.
admin.site.register(Plato, PlatoAdmin)
admin.site.register(Categoria)
admin.site.register(Proveedor)
admin.site.register(Profile)
admin.site.register(Menu)
admin.site.register(DetalleMenu)