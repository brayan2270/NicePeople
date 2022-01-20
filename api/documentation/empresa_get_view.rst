======================================
 Recurso que Trae los Puntos de Acceso
======================================


Recurso GET
------------
.. http:post:: /api/v1/empresa

Autentica al usuario y Trae los puntos de acceso de la empresa.


**Ejemplo de petición**

.. sourcecode:: http

    GET /api/v1/empresa HTTP/1.1
    Content-Type: application/json

**Ejemplos de respuesta**

.. sourcecode:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "status code": 200,
        "empresa": "prueba1",
        "message": "access points",
        "data": [
            {
                "id": 9,
                "nombre": "prueba1",
                "direccion": "qqqq11",
                "email": "pruebaacceso@gmail.com",
                "geolocalizacion": "(123)(12312)",
                "estado": true,
                "empresa": 1
            }
        ]
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


:status 200: access points
:status 403: No tiene los permisos necesarios
:status 401: El token es incorrecto o expiro