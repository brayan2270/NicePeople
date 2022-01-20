from curses.ascii import US
from re import U
from django.db import models

class Empresa(models.Model):
    
    nit = models.CharField(max_length=100)
    nombre_empresa = models.CharField(max_length=200)
    nombre_comercial_empresa = models.CharField(max_length=200)
    direccion = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    sitio_web = models.URLField()
    ciudad = models.CharField("Ciudad", max_length=100, blank=True)
    pais = models.CharField("Pais", max_length=100, blank=True)
    departamento = models.CharField("Departamento", max_length=100, blank=True)




    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
        app_label = 'api'

    def __str__(self):
        return '{}'.format(self.nombre_empresa)
