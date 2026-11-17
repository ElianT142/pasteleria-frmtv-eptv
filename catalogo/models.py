from django.db import models
from django.utils import timezone
import uuid

# Create your models here.
class linea(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.nombre
    
class producto(models.Model):
    nombre = models.CharField(max_length=50)
    linea = models.ForeignKey(linea, on_delete=models.CASCADE, related_name='productos')
    precio = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='imagenes/', blank=True, null=True)
    apto_celiacos = models.BooleanField(default=False)
    cantidad = models.PositiveSmallIntegerField(verbose_name='porciones')
    disponibilidad = models.BooleanField(default=True)
    stock_dia = models.PositiveIntegerField(verbose_name='stock del día')

    class Meta:
        ordering = ['nombre']
        verbose_name_plural = 'productos de la pasteleria'

    def __str__(self):
        return self.nombre

    @property
    def agotado(self):
        return self.stock_dia == 0
  
class encargo(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    fecha_encargo = models.DateTimeField(auto_now_add=True)
    cantidad = models.PositiveSmallIntegerField()
    fecha_retiro = models.DateField()
    codigo = models.CharField(max_length=10, unique=True, blank=True, editable=False)
    producto = models.ForeignKey(producto, on_delete=models.CASCADE, related_name='encargos')

    class Meta:
        ordering = ['-fecha_encargo']
        verbose_name_plural = 'encargos'

    def save(self, *args, **kwargs):
        if not self.codigo:
            self.codigo = uuid.uuid4().hex[:8].upper()
        super().save(*args, **kwargs)

    @property
    def total(self):
        return self.cantidad * self.producto.precio

    def __str__(self):
        return f'{self.codigo} - {self.nombre}'

