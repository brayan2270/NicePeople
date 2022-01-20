from django.db import models
from django.contrib.auth.models import AbstractUser
from .profile import Profile
from .empresa import Empresa



class User(AbstractUser):
    """Extends native django user model adding new
       features to user definition.

    """

    creation_date = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(blank=True, null=True, verbose_name='last login')
    
    cellphone = models.CharField("Celular", max_length=11, blank=True)
    departamento = models.CharField("Departamento", max_length=100, blank=True)
    ciudad = models.CharField("Ciudad", max_length=100, blank=True)
    pais = models.CharField("Pais", max_length=100, blank=True)
    address = models.CharField("Direccion", max_length=100, blank=True)
   
    profile = models.ManyToManyField(Profile, related_name='user_profile')
    is_activate = models.BooleanField("Registrado", default=False)

    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True, blank=True)

    REQUIRED_FIELDS = ['email']

    class Meta:  # pylint: disable=too-few-public-methods
        """ Sets human readable name """
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        app_label = 'api'

    def __str__(self):
        return '{} - {}'.format(self.pk, self.email)



