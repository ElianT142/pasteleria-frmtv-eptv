from django.contrib import admin
from .models import linea, producto, encargo

# Register your models here.
def formato_clp(valor):
    
    if valor is None:
        return ''
    return '$' + f'{int(valor):,}'.replace(',', '.')

@admin.register(linea)
class lineaAdmin(admin.ModelAdmin):
    list_display=('nombre',)

@admin.register(producto)
class productoAdmin(admin.ModelAdmin):
    list_display=('nombre','precio_clp','apto_celiacos','cantidad','disponibilidad','stock_dia',)
    @admin.display(description='Precio', ordering='precio')
    def precio_clp(self, obj):
        return formato_clp(obj.precio)
    
@admin.register(encargo)
class encargoAdmin(admin.ModelAdmin):
    list_display=('nombre','fecha_encargo','codigo','producto','cantidad','fecha_retiro','total_clp',)
