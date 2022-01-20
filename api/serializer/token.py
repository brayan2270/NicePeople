import jwt
import datetime as dt


from rest_framework import serializers

from django.contrib.auth import authenticate
from django.utils.crypto import get_random_string
from django.conf import settings
from django.utils import timezone


from ..models import Auth, User

class AuthSerializer(serializers.Serializer):

    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    keep_logged_in = serializers.BooleanField(default=False)
    token = serializers.CharField(max_length=255, read_only = True)


    def validate(self, data):
        username = data.get("username", None)
        password = data.get("password", None)
        keep_logged_in = data.get("keep_logged_in", None)
        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password is not found.'
            )

        user_active = User.objects.filter(pk=user.pk).first()
        
        if user_active.is_activate == False:
            
            raise serializers.ValidationError(
                'The user is not active.'
            )

        user_profile = User.objects.filter(pk=user.pk).values_list('profile__profile', flat=True)
        

        refresh = get_random_string(30)
        prueba = jwt.encode({
            'expiration_date': str(
                (
                    dt.datetime.now() +
                    dt.timedelta(
                        days=settings.TOKEN_EXP_DAYS
                        if not keep_logged_in
                        else settings.KEEP_LOGGED_IN_TOKEN_EXP_DAYS
                    )
                )
            ),
            'email': user.email,
            'roles': user_profile[0],
            'refresh': refresh
        }, settings.SECRET_KEY, algorithm='HS256')


        model = Auth.objects.create(token=str(prueba))
        
        User.objects.filter(
            pk=user.pk
        ).update(last_login=timezone.now())

        return {
            'username': str(user.username),
            'token': str(prueba),
        }