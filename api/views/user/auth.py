from dataclasses import asdict
from datetime import datetime, timedelta

from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from ...serializer.token import AuthSerializer
from ...serializer.acceso_user import AccesoUserSerializer

from ...helpers.profile_names import ADMINISTRATOR, ENTERPRISE_ADMINISTRATOR, COMPANY_EMPLOYEE
from ...helpers.email import email_service
from ...helpers.email_template import get_session

from ...models import User, HorarioAcceso, PuntoAccesoEmpresa
class UserLoginView(APIView):

    serializer_class = AuthSerializer

    def post(self, request):
        data = User.objects.filter(username=request.data['username']).first()

        user = User.objects.filter(username=request.data['username']).values_list('profile__profile', flat=True)
        user_empresa = User.objects.filter(username=request.data['username']).values_list('empresa', flat=True)
        user_email_error = User.objects.filter(empresa=user_empresa[0], profile=2).first()
        
        if user[0] == COMPANY_EMPLOYEE:

            horario_acceso = HorarioAcceso.objects.filter(user__username=request.data['username'])
            contador = 0
            contador2 = 0
            if horario_acceso:
                

                current_time = datetime.now()
                current_time_str = current_time.strftime('%Y-%m-%d %H:%M:%S')
                current_time_date = datetime.strptime(current_time_str, '%Y-%m-%d %H:%M:%S')

                for date in horario_acceso:
                    date_time = date.horario_fin.strftime('%Y-%m-%d %H:%M:%S')
                    date2 = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')
                    if date.punto_acceso.estado == True:
                        
                        if current_time_date > date2:
                            contador += 1
                            print("profile: ",date.delete())
                        else:
                            contador2 += 1
                    else:
                        contador += 1

            if contador2 > 0:
                
                serializer = AuthSerializer(data=request.data)
                if not serializer.is_valid():
                    return Response({
                        'code': 'invalid_body',
                        'detailed': 'Cuerpo de la petición con estructura inválida',
                        'data': serializer.errors
                    }, status=status.HTTP_400_BAD_REQUEST)
                
                horario_acceso = HorarioAcceso.objects.filter(user__username=request.data['username'])
                response = {
                    'status code' : status.HTTP_200_OK,
                    'message': 'User logged in  successfully',
                    'token' : serializer.data['token'],
                    "Horario_acceso": AccesoUserSerializer(horario_acceso, many=True).data
                    }
                status_code = status.HTTP_200_OK

                return Response(response, status=status_code)
            
            elif contador >= 0:
                
                serializer = AuthSerializer(data=request.data)
                if not serializer.is_valid():
                    return Response({
                        'code': 'invalid_body',
                        'detailed': 'Cuerpo de la petición con estructura inválida',
                        'data': serializer.errors
                    }, status=status.HTTP_400_BAD_REQUEST)

                email_service({
                "subject": "Creacion de Usuario",
                "body": get_session(user_email_error.first_name, user_email_error.last_name, request.data['username'], data.first_name, data.last_name),
                "email": [user_email_error.email]
                })

                return Response({
                    "code": "invalid_request",
                    "detailed": "No se puede acceder porque su franja horaria caduco o la sede esta inactiva"
                }, status=status.HTTP_403_FORBIDDEN)

        serializer = AuthSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                'code': 'invalid_body',
                'detailed': 'Cuerpo de la petición con estructura inválida',
                'data': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        response = {
            'status code' : status.HTTP_200_OK,
            'message': 'User logged in  successfully',
            'token' : serializer.data['token'],
            }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)