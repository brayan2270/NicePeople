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

from ...models import ActivateUser, User, Empresa

from ...helpers.profile_names import ADMINISTRATOR, ENTERPRISE_ADMINISTRATOR, COMPANY_EMPLOYEE
from ...helpers.token import TokenHandler
from ...helpers.email import email_service
from ...helpers.email_template import get_email_user, get_Activate_user

class UserRegisterView(APIView, TokenHandler):

    serializer_class = UserRegisterSerializer

    def post(self, request):

        payload, user = self.get_payload(request)
        if not payload:
                return Response({
                    "code": "unauthorized",
                    "detailed": "El token es incorrecto o expiro"
                }, status=status.HTTP_401_UNAUTHORIZED)

        if not self.has_permissions([ADMINISTRATOR], user):
            return Response({
                "code": "invalid_request",
                "detailed": "No tiene los permisos necesarios"
            }, status=status.HTTP_403_FORBIDDEN)

        

        request.data['username'] = request.data['email']
        request.data['is_activate'] = False

        

        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response({
                'code': 'invalid_body',
                'detailed': 'Cuerpo de la petición con estructura inválida',
                'data': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)


        request.data['empresa'] = Empresa.objects.filter(pk=request.data['empresa']).first()

        profile = request.data["profile"]
        capture = request.data
        capture.pop('profile', request.data['profile'])
        

        if profile == "1":
            profile = ADMINISTRATOR

        elif profile == "2":
            profile = ENTERPRISE_ADMINISTRATOR

        elif profile == "3":
            profile = COMPANY_EMPLOYEE

        
        
        data = serializer.create(capture, profile)
        
        user = User.objects.filter(email=request.data['email'], is_activate=False).first()
        print("data: ",user)
        if user:
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
                "email": [request.data['email']]
            })

        if profile == ENTERPRISE_ADMINISTRATOR:
            email_service({
                "subject": "Creacion de Usuario",
                "body": get_email_user(request.data['first_name'], request.data['last_name'], request.data['email'], request.data['password']),
                "email": [request.data['email']]
            })

        
        response = {
            'status code' : status.HTTP_201_CREATED,
            'message': 'User created successfully',
            'inserted' : data.pk,
            }
        status_code = status.HTTP_201_CREATED

        return Response(response, status=status_code)