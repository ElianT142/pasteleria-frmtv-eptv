from django.db import models

# Create your models here.
class linea(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

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
    nombre = models.CharField(max_length=10)
    correo = models.CharField(max_length=10)
    fecha_encargo = models.DateField()
    cantidad = models.SmallIntegerField()
    fecha_retiro = models.DateTimeField()
    codigo = models.CharField(max_length=10, unique=True)
    producto = models.ForeignKey(producto, on_delete=models.CASCADE, related_name='encargo')
    class Meta:
        ordering = ['nombre']
        verbose_name_plural = 'encargos'
    def __str__(self):
        return self.nombre

