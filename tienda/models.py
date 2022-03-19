from django.db import models

# Create your models here.
class Vendedor(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=30)
    codigoEmpleado = models.IntegerField()
    empleado = models.BooleanField()
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=30)
    dni= models.IntegerField()
    
class Producto(models.Model):
    nombre = models.CharField(max_length=25)
    marca = models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=100, decimal_places=2)
    codigoProducto = models.IntegerField()
    cantidad = models.IntegerField()
    
    def __str__(self):
        return f'{self.nombre} {self.marca}'