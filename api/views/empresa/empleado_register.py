from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from django.core.mail import send_mail
from django.conf import settings

from ...serializer.user_register import UserRegisterSerializer


from ...helpers.profile_names import ADMINISTRATOR, ENTERPRISE_ADMINISTRATOR, COMPANY_EMPLOYEE
from ...helpers.token import TokenHandler
from ...helpers.email import email_service
from ...helpers.email_template import get_email_user

from ...models import Empresa

class EmpleadoRegisterView(APIView, TokenHandler):

    serializer_class = UserRegisterSerializer

    def post(self, request, pk):

        request.data['username'] = request.data['email']

        request.data['empresa'] = Empresa.objects.filter(pk=pk).first()
        print("hola2")
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response({
                'code': 'invalid_body',
                'detailed': 'Cuerpo de la petición con estructura inválida',
                'data': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)


        profile = COMPANY_EMPLOYEE
        capture = request.data

        
        
        data = serializer.create(capture, profile)
        
        
        response = {
            'status code' : status.HTTP_201_CREATED,
            'message': 'User created successfully',
            'inserted' : data.pk,
            }
        status_code = status.HTTP_201_CREATED

        return Response(response, status=status_code)