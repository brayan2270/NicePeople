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

class EmailUserActivateView(APIView, TokenHandler):

    def post(self, request, *args, **kwargs):
        print("data: ",kwargs)
        user = User.objects.filter(email=kwargs['email']).first()

        if user.is_activate == True:
            return Response({
                "code": "user_activate",
                "detailed": "el usuario ya se encuentra activato"
            }, status=status.HTTP_400_BAD_REQUEST)

        token = get_random_string(70)
        ActivateUser.objects.create(
            expiration_date=(timezone.now() +
                            dt.timedelta(days=int(settings.TOKEN_EXP_DAYS))),
            is_used=False,
            token=token,
            user=user)

        email_service({
            "subject": "Activar Usuario",
            "body": get_Activate_user(user.first_name, user.last_name, token),
            "email": [kwargs["email"]]
        })

        response = {
            'status code' : status.HTTP_200_OK,
            'message': 'mail sent successfully'
            }

        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)