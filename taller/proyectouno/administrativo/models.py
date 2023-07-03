from django.db import models

# Create your models here.
from django.db import models

class Edificio(models.Model):
    TIPO_CHOICES = (
        ('residencial', 'Residencial'),
        ('comercial', 'Comercial'),
    )
    
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)

    def __str__(self):
        return self.nombre


class Departamento(models.Model):
    propietario = models.CharField(max_length=200)
    costo = models.DecimalField(max_digits=8, decimal_places=2)
    numero_cuartos = models.PositiveIntegerField()
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE)

    def __str__(self):
        return self.propietario

