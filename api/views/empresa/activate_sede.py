from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response


from ...serializer.empresa import EmpresaSerializer


from ...helpers.profile_names import ADMINISTRATOR, ENTERPRISE_ADMINISTRATOR, COMPANY_EMPLOYEE
from ...helpers.token import TokenHandler
from ...helpers.email import email_service
from ...helpers.email_template import get_email_employee

from ...models import User, PuntoAccesoEmpresa

class ActivateSedeView(RetrieveAPIView, TokenHandler):


    def patch(self, request, pk):

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

        if request.data.get('estado') == None:
            return Response({
                "code": "invalid_body",
                "detailed": "Cuerpo con estructura inválida"
            }, status=status.HTTP_400_BAD_REQUEST)

        PuntoAccesoEmpresa.objects.filter(pk=pk).update(estado=request.data['estado'])


        response = {
            'status code' : status.HTTP_200_OK,
            'message': 'headquarters status updated',
            'sede': request.data['estado'],
            }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)