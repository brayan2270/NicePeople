from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response


from ...serializer.empresa import EmpresaSerializer


from ...helpers.profile_names import ADMINISTRATOR, ENTERPRISE_ADMINISTRATOR, COMPANY_EMPLOYEE
from ...helpers.token import TokenHandler
from ...helpers.email import email_service
from ...helpers.email_template import get_email_employee

from ...models import User, Empresa

class EmpleadoEmailView(RetrieveAPIView, TokenHandler):


    def post(self, request, email):

        payload, user = self.get_payload(request)
        if not payload:
                return Response({
                    "code": "unauthorized",
                    "detailed": "El token es incorrecto o expiro"
                }, status=status.HTTP_401_UNAUTHORIZED)

        if not self.has_permissions([ENTERPRISE_ADMINISTRATOR], user):
            return Response({
                "code": "invalid_request",
                "detailed": "No tiene los permisos necesarios"
            }, status=status.HTTP_403_FORBIDDEN)       


        user = User.objects.filter(email=payload['email']).values_list('empresa', flat=True)
        empresa = Empresa.objects.filter(pk=user[0]).values_list('nombre_empresa', flat=True).first()

        email_service({
            "subject": "Creacion de Usuario",
            "body": get_email_employee(empresa[0], user[0]),
            "email": [email]
        })


        response = {
            'status code' : status.HTTP_200_OK,
            'message': 'email sent successfully',
            'email' : email,
            }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)