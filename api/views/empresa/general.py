from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from ...serializer.empresa import EmpresaSerializer
from ...helpers.profile_names import ADMINISTRATOR, ENTERPRISE_ADMINISTRATOR, COMPANY_EMPLOYEE
from ...helpers.token import TokenHandler


class EmpresaView(RetrieveAPIView, TokenHandler):

    serializer_class = EmpresaSerializer

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
            'message': 'successfully created company',
            'inserted' : data.pk,
            }
        status_code = status.HTTP_201_CREATED

        return Response(response, status=status_code)

