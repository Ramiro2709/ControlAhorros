from django.contrib import admin

from Registro.models import Categoria,Subcategoria,Moneda,Tipo_fondo,Plataforma


class CategoriaAdmin(admin.ModelAdmin):
    list_display=("nombre",)
    list_filter=("nombre",)
    #date_hierarchy="date" # Filtro superior,

class SubcategoriaAdmin(admin.ModelAdmin):
    list_display=("nombre","categoria")

class MonedaAdmin(admin.ModelAdmin):
    list_display=("nombre","sigla")

class PlataformaAdmin(admin.ModelAdmin):
    list_display=("nombre",)

# Para guardar el modelo
admin.site.register(Categoria, CategoriaAdmin)

admin.site.register(Subcategoria, SubcategoriaAdmin)

admin.site.register(Moneda,MonedaAdmin)

admin.site.register(Tipo_fondo)

admin.site.register(Plataforma,PlataformaAdmin)