import email
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from ...serializer.punto_acceso import GetPuntoAccesoSerializer
from ...helpers.profile_names import ADMINISTRATOR, ENTERPRISE_ADMINISTRATOR, COMPANY_EMPLOYEE
from ...helpers.token import TokenHandler
from ...models import Empresa, User, PuntoAccesoEmpresa

class EmpresaGetView(RetrieveAPIView, TokenHandler):

    serializer_class = GetPuntoAccesoSerializer

    def get(self, request):

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
        empresa = Empresa.objects.filter(pk=user[0]).values_list('nombre_empresa', flat=True)
        print("data: ",user)

        puntos_acceso = PuntoAccesoEmpresa.objects.filter(empresa__pk=user[0])
        
        serializer = self.serializer_class(puntos_acceso, many=True)

        response = {
            'status code' : status.HTTP_200_OK,
            'empresa': empresa[0],
            'message': 'access points',
            'data' : serializer.data,
            }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)

