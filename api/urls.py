from django.urls import path
from .views.user.auth import UserLoginView
from .views.user.user import UserRegisterView
from .views.user.activate_user import UserActivateView
from .views.user.email_activate_user import EmailUserActivateView
from .views.empresa.general import EmpresaView
from .views.empresa.puntos_acceso import PuntoAccesoView
from .views.empresa.empleado_email import EmpleadoEmailView
from .views.empresa.empleado_register import EmpleadoRegisterView
from .views.empresa.empresa import EmpresaGetView
from .views.empresa.acceso_user import AceesoUserView
from .views.empresa.activate_sede import ActivateSedeView




app_name = 'api'

urlpatterns = [
    path('auth', UserLoginView.as_view(), name='auth'),
    path('user/register', UserRegisterView.as_view(), name='user_register'),
    path('empresa/register', EmpresaView.as_view(), name='empresa_register'),
    path('punto/acceso', PuntoAccesoView.as_view(), name='punto_acceso'),
    path('activate/sede/<int:pk>', ActivateSedeView.as_view(), name='activate_sede'),
    path('empleado/email/<str:email>', EmpleadoEmailView.as_view(), name='empleado_email'),
    path('empleado/register/<int:pk>', EmpleadoRegisterView.as_view(), name='empleado_register'),
    path('empresa', EmpresaGetView.as_view(), name='empresa'),
    path('acceso/user/<int:punto_acceso>', AceesoUserView.as_view(), name='acceso_user'),
    path('user/activate/<str:token>', UserActivateView.as_view(), name='activate_user'),
    path('user/activate/email/<str:email>', EmailUserActivateView.as_view(), name='activate_email'),

]
