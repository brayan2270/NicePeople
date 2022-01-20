from django.db import models
from .user import User
from .punto_acceso import PuntoAccesoEmpresa

class HorarioAcceso(models.Model):
    
    punto_acceso = models.ForeignKey(PuntoAccesoEmpresa, on_delete=models.CASCADE, null=True, blank=True)
    horario_inicio = models.DateTimeField()
    horario_fin = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


      
    class Meta:
        verbose_name = "Horario Acceso"
        verbose_name_plural = "Horarios Acceso"
        app_label = 'api'

    def __str__(self):
        return '{}'.format(self.punto_acceso)
