import datetime as dt

from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone

from ...serializer.user_register import UserRegisterSerializer

from ...models import ActivateUser, User

from ...helpers.profile_names import ADMINISTRATOR, ENTERPRISE_ADMINISTRATOR, COMPANY_EMPLOYEE
from ...helpers.token import TokenHandler
from ...helpers.email import email_service
from ...helpers.email_template import get_email_user, get_Activate_user

class UserActivateView(APIView, TokenHandler):


    def patch(self, request, *args, **kwargs):

        activate = ActivateUser.objects.filter(token=kwargs["token"]).first()

        if not activate:
            return Response({
                "code": "token_not_found",
                "detailed": "Token no encontrado"
            }, status=status.HTTP_404_NOT_FOUND)


        if (activate.is_used or
                dt.datetime.now() >= activate.expiration_date.replace(
                    tzinfo=None)):
            ActivateUser.objects.filter(
                token=kwargs["token"]).delete()
            return Response({
                "code": "token_expired_or_used",
                "detailed": "Token ya usado o vencido"
            }, status=status.HTTP_202_ACCEPTED)

        User.objects.filter(email=activate.user.email).update(
            is_activate=True)

        ActivateUser.objects.filter(
            token=kwargs["token"]).update(is_used=True)



        response = {
            'status code' : status.HTTP_200_OK,
            'message': 'User activated successfully'
            }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)
    