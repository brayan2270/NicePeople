from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.core.mail import send_mail
from django.conf import settings

from ...serializer.punto_acceso import PuntoAccesoSerializer


from ...helpers.profile_names import ADMINISTRATOR, ENTERPRISE_ADMINISTRATOR, COMPANY_EMPLOYEE
from ...helpers.token import TokenHandler

from ...models import User, Empresa, PuntoAccesoEmpresa

class PuntoAccesoView(APIView, TokenHandler):

    serializer_class = PuntoAccesoSerializer

    def post(self, request):

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

        empresa = Empresa.objects.filter(id=user[0]).first()

        
        request.data['empresa'] = empresa

        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response({
                'code': 'invalid_body',
                'detailed': 'Cuerpo de la petición con estructura inválida',
                'data': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        print("dat: ",empresa)
        data = serializer.create(request.data)

        
        response = {
            'status code' : status.HTTP_201_CREATED,
            'message': 'hotspot created successfully',
            'inserted' : data.pk,
            }
        status_code = status.HTTP_201_CREATED

        return Response(response, status=status_code)