import jwt
import datetime as dt
import copy
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


from django.utils.crypto import get_random_string
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

from ..services.user_register import UserProfiles

from ..models import Auth, User, Profile


USER = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    """ Defines profile serializer behaviour. """

    class Meta:  # pylint: disable=too-few-public-methods
        """ Defines serializer fields that are being used """

        model = Profile
        fields = ['profile']

class UserRegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=USER.objects.all())]
    )
    profile = ProfileSerializer(read_only=True, many=True)
    
    cellphone = serializers.CharField(required=True)
    departamento = serializers.CharField(required=True)
    ciudad = serializers.CharField(required=True)
    pais = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'profile', 'cellphone', 'departamento', 'ciudad', 'pais', 'address',
        'is_activate', 'first_name', 'last_name']


    def create(self, validated_data, profile):
        """ Creates an user object with its password and relate it with
            its profiles.

        Parameters:
            validated_data (dict):Contains the data from user that is going to
                                  be created.

        Returns:
            user (User): A fields-full custom django user.

        """


        aux = copy.deepcopy(validated_data)

        aux['username'] = aux['email'].lower()
        aux['email'] = aux['email'].lower()
        aux['password'] = make_password(validated_data['password'])

        user = USER.objects.create(**aux)
        user = UserProfiles(user).add_profile(profile)
        user.save()

        return user