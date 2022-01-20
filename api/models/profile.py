from django.db import models


class Profile(models.Model):
    """ Profile model """

    profile = models.CharField(
        "Nombres", max_length=255)

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"
        app_label = 'api'

    def __str__(self):
        return self.profile