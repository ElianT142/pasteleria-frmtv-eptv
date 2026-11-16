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
    list_display=('nombre','precio_clp','apto_celiacos',)
    @admin.display(description='Precio', ordering='precio')
    def precio_clp(self, obj):
        return formato_clp(obj.precio)
    
@admin.register(encargo)
class encargoAdmin(admin.ModelAdmin):
    list_display=('nombre','fecha_encargo','codigo','producto','total_original_clp','total_descuento_clp','total_final_clp',)
    @admin.display(description='Total original', ordering='total_original')
    def total_original_clp(self, obj):
        return formato_clp(obj.total_original)

    @admin.display(description='Total descuento', ordering='total_descuento')
    def total_descuento_clp(self, obj):
        return formato_clp(obj.total_descuento)

    @admin.display(description='Total final', ordering='total_final')
    def total_final_clp(self, obj):
        return formato_clp(obj.total_final)