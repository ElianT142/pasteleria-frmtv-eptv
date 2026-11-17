from django.contrib import admin
from .models import linea, producto, encargo
from django.utils.html import format_html
from .templatetags.formato import clp

admin.site.site_header = 'Administración de Pastelería FRMTV'
admin.site.site_title = 'Pastelería FRMTV'
admin.site.index_title = 'Gestión del catálogo y los encargos'

@admin.register(linea)
class lineaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(producto)
class productoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'miniatura', 'linea', 'disponibilidad', 'stock_dia', 'precio_clp', 'apto_celiacos')
    list_filter = ('linea', 'apto_celiacos')
    search_fields = ('nombre',)

    @admin.display(description='Precio', ordering='precio')
    def precio_clp(self, obj):
        return clp(obj.precio)

    @admin.display(description='Foto')
    def miniatura(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" style="height:60px; border-radius:4px;">', obj.imagen.url)
        return '-'

@admin.register(encargo)
class encargoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'producto', 'nombre', 'cantidad', 'fecha_retiro')
    list_filter = ('producto', 'fecha_retiro')
    search_fields = ('nombre', 'correo')