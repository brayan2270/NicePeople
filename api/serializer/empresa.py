import jwt
import datetime as dt


from rest_framework import serializers

from django.contrib.auth import authenticate
from django.utils.crypto import get_random_string
from django.conf import settings
from django.utils import timezone


from ..models import Auth, User, Empresa

class EmpresaSerializer(serializers.ModelSerializer):

    nit = serializers.CharField(required=True)
    nombre_empresa = serializers.CharField(required=True)
    nombre_comercial_empresa = serializers.CharField(required=True)
    direccion = serializers.CharField(required=True)
    telephone = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    sitio_web = serializers.URLField(required=True)
    ciudad = serializers.CharField(required=True)
    pais = serializers.CharField(required=True)
    departamento = serializers.CharField(required=True)

    class Meta:
        model = Empresa
        fields = '__all__'