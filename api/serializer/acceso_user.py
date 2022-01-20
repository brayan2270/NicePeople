import imp
from re import T
import jwt
import datetime as dt


from rest_framework import serializers

from django.contrib.auth import authenticate
from django.utils.crypto import get_random_string
from django.conf import settings
from django.utils import timezone

from .user_register import UserRegisterSerializer
from .punto_acceso import GetPuntoAccesoSerializer

from ..models import Auth, User, Empresa, HorarioAcceso

class AccesoUserSerializer(serializers.ModelSerializer):

    punto_acceso = GetPuntoAccesoSerializer(read_only=True)
    horario_inicio = serializers.DateTimeField(required=True)
    horario_fin = serializers.DateTimeField(required=True)
    user = UserRegisterSerializer(read_only=True)

    class Meta:
        model = HorarioAcceso
        fields = '__all__'