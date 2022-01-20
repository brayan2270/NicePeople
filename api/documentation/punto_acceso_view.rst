=======================================
 Recurso de Creacion de Punto de Acceso
=======================================


Recurso POST
------------
.. http:post:: /api/v1/punto/acceso

Autentica al usuario y Punto de Acceso.

**Campos obligatorios**

:nombre: **(string)** Nombre del punto de acceso
:direccion: **(string)** Direccion del punto de acceso
:email: **(string)** Email del punto de acceso
:geolocalizacion: **(string)** Geolocalizacion del punto de acceso


**Ejemplo de petición**

.. sourcecode:: http

    POST /api/v1/punto/acceso HTTP/1.1
    Content-Type: application/json

    {
        "nombre": "prueba1",
        "direccion": "qqqq11",
        "email": "pruebaacceso@gmail.com",
        "geolocalizacion": "(123)(12312)"
    }

**Ejemplos de respuesta**

.. sourcecode:: http

    HTTP/1.1 201 CREATED
    Content-Type: application/json

    {
        "status code": 201,
        "message": "hotspot created successfully",
        "inserted": 20
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

    HTTP/1.1 400 BAD_REQUEST
    Content-Type: application/json

    {
        "code": "invalid_body",
        "detailed": "Cuerpo de la petición con estructura inválida"
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


:status 201: hotspot created successfully
:status 400: Cuerpo de la petición con estructura inválida
:status 403: No tiene los permisos necesarios
:status 401: El token es incorrecto o expiro