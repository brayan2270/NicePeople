from operator import mod
from django.db import models
from .empresa import Empresa

class PuntoAccesoEmpresa(models.Model):
    
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    geolocalizacion = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)


    
    class Meta:
        verbose_name = "Punto Acceso"
        verbose_name_plural = "Puntos Acceso"
        app_label = 'api'

    def __str__(self):
        return '{}'.format(self.nombre)
