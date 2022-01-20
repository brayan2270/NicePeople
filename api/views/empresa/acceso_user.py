from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response


from ...serializer.acceso_user import AccesoUserSerializer


from ...helpers.profile_names import ADMINISTRATOR, ENTERPRISE_ADMINISTRATOR, COMPANY_EMPLOYEE
from ...helpers.token import TokenHandler
from ...helpers.email import email_service
from ...helpers.email_template import get_email_employee

from ...models import User, Empresa, PuntoAccesoEmpresa

class AceesoUserView(APIView, TokenHandler):

    serializer_class = AccesoUserSerializer

    def post(self, request, punto_acceso):

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


        punto_acceso_user = PuntoAccesoEmpresa.objects.filter(pk=punto_acceso).values_list('empresa', flat=True)
        empresa_user = User.objects.filter(email=payload['email']).values_list('empresa', flat=True)

        if punto_acceso_user[0] != empresa_user[0]:
            return Response({
                    "code": "incorrect_information",
                    "detailed": "El punto de acceso no pertenece a la empresa que tienes asignada"
                }, status=status.HTTP_409_CONFLICT)




        user = User.objects.filter(pk=request.data['user']).first()
        punto_acceso = PuntoAccesoEmpresa.objects.filter(pk=punto_acceso).first()
        request.data['user'] = user
        request.data['punto_acceso'] = punto_acceso

        serializer = self.serializer_class(data=request.data)
        
        if not serializer.is_valid():
            return Response({
                'code': 'invalid_body',
                'detailed': 'Cuerpo de la petición con estructura inválida',
                'data': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)


        data = serializer.create(request.data)



        response = {
            'status code' : status.HTTP_201_CREATED,
            'message': 'email sent successfully',
            'inserted' : data.pk,
            }
        status_code = status.HTTP_201_CREATED

        return Response(response, status=status_code)