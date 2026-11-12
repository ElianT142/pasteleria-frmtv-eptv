from django.contrib import admin
from .models import linea, producto, encargo

# Register your models here.

@admin.register(linea)
class lineaAdmin(admin.ModelAdmin):
    list_display:()

@admin.register(producto)
class productoAdmin(admin.ModelAdmin):
    list_display:()

@admin.register(encargo)
class encargoAdmin(admin.ModelAdmin):
    list_display:()