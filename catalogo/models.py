from django.db import models
from django.utils import timezone

# Create your models here.
class linea(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.nombre
    
class producto(models.Model):
    nombre = models.CharField(max_length=50)
    linea = models.ForeignKey(linea, on_delete=models.CASCADE, related_name='producto')
    precio = models.SmallIntegerField()
    imagen = models.ImageField(upload_to='imagenes/', blank=True, null=True)
    apto_celiacos = models.BooleanField(default=False)
    cantidad = models.SmallIntegerField()
    disponibilidad = models.BooleanField(default=True)
    stock_dia = models.SmallIntegerField()

    class Meta:
        ordering = ['nombre']
        verbose_name_plural = 'productos de la pasteleria'

    def __str__(self):
        return self.nombre
    
class encargo(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100, blank=True)
    fecha_encargo = models.DateTimeField(auto_now_add=True)
    cantidad = models.SmallIntegerField()
    fecha_retiro = models.DateField()
    codigo = models.CharField(max_length=10, blank=True, null=True)
    producto = models.ForeignKey(producto, on_delete=models.CASCADE, related_name='encargo')
    total_original_clp = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_descuento_clp = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_final_clp = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        ordering = ['nombre']
        verbose_name_plural = 'encargos'
    def __str__(self):
        return self.nombre

