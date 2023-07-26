from django.core.validators import MinValueValidator
from datetime import date
from django.db import models

# Create your models here.

# Registros de laboratorios
class Laboratorio(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100, default='nulo')
    pais = models.CharField(max_length=100, default='nulo')

    def __str__(self) -> str:
        return self.nombre


# Registro de directores generales
class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=100, default='nulo')

    def __str__(self) -> str:
        return self.nombre


# Registr de productos
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    f_fabricacion = models.DateField(validators=[MinValueValidator(date(2015, 1, 1))])
    p_costo = models.DecimalField(max_digits=10, decimal_places=2)
    p_venta = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.nombre} tiene un valor de venta: {self.p_venta}'
