=========================================================
 Recurso de Envio de Email para Creacion Usuario Empleado
=========================================================


Recurso POST
------------
.. http:post:: /api/v1/empleado/email/<str:email>

Autentica al usuario y envia email para creacion de usuario empleado


**Ejemplo de petición**

.. sourcecode:: http

    POST /api/v1/empleado/email/prueba@gmail.com HTTP/1.1
    Content-Type: application/json


**Ejemplos de respuesta**

.. sourcecode:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "status code": 200,
        "message": "email sent successfully",
        "email": "prueba@gmail.com"
    }


HTTP/1.1 403 FORBIDDEN
    Content-Type: application/json

    {
        {
            "code": "invalid_request",
            "detailed": "No tiene los permisos necesarios"
        }
    }



.. sourcecode:: http

    HTTP/1.1 401 UNAUTHORIZED
    Content-Type: application/json

    {
        {
            "code": "unauthorized",
            "detailed": "El token es incorrecto o expiro"
        }
    }


:status 200: email sent successfully
:status 403: No tiene los permisos necesarios
:status 401: El token es incorrecto o expiro