""" Contains the Password recovery model """

from django.db import models
from .user import User


class ActivateUser(models.Model):

    creation_date = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField("Fecha de vencimiento")
    is_used = models.BooleanField("Fue usado", default=False)
    token = models.TextField("Token", max_length=700)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:  # pylint: disable=too-few-public-methods
        """ Sets human readable name """
        verbose_name = "Activar de usuario"
        verbose_name_plural = "Activar de usuarios"
        app_label = 'api'

    def __str__(self):
        # pylint: disable=no-member
        return self.user.email
