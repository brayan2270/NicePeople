import jwt
import datetime as dt


from rest_framework import serializers

from django.contrib.auth import authenticate
from django.utils.crypto import get_random_string
from django.conf import settings
from django.utils import timezone

from .empresa import EmpresaSerializer

from ..models import Auth, User, Empresa, PuntoAccesoEmpresa

class PuntoAccesoSerializer(serializers.ModelSerializer):

    nombre = serializers.CharField(required=True)
    direccion = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    empresa = EmpresaSerializer(read_only=True)
    geolocalizacion = serializers.CharField(required=True)

    class Meta:
        model = PuntoAccesoEmpresa
        fields = '__all__'



class GetPuntoAccesoSerializer(serializers.ModelSerializer):

    nombre = serializers.CharField(required=True)
    direccion = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    geolocalizacion = serializers.CharField(required=True)

    class Meta:
        model = PuntoAccesoEmpresa
        fields = '__all__'