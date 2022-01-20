======================================
 Recurso de Creacion de Horario Acceso
======================================


Recurso POST
------------
.. http:post:: /api/v1/acceso/user/<int:punto_acceso>

Autentica al usuario y crea el horario de acceso.

**Campos obligatorios**

:nombre: **(string)** Nombre del punto de acceso
:direccion: **(string)** Direccion del punto de acceso
:email: **(string)** Email del punto de acceso
:geolocalizacion: **(string)** Geolocalizacion del punto de acceso

user: **(integer)** id del usuario empleado
horario_inicio: **(string)** hora inicio del punto de acceso
horario_fin: **(string)** hora final del punto de acceso


**Ejemplo de petición**

.. sourcecode:: http

    POST /api/v1/acceso/user/1 HTTP/1.1
    Content-Type: application/json

    {
        "user": 1,
        "horario_inicio": "2022-01-19 16:30",
        "horario_fin": "2022-01-23 16:30"
    }

**Ejemplos de respuesta**

.. sourcecode:: http

    HTTP/1.1 201 CREATED
    Content-Type: application/json

    {
        "status code": 201,
        "message": "email sent successfully",
        "inserted": 5
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


.. sourcecode:: http

    HTTP/1.1 409 CONFLICT
    Content-Type: application/json

    {
        {
            "code": "incorrect_information",
            "detailed": "El punto de acceso no pertenece a la empresa que tienes asignada"
        }
    }



:status 201: hotspot created successfully
:status 400: Cuerpo de la petición con estructura inválida
:status 403: No tiene los permisos necesarios
:status 401: El token es incorrecto o expiro
:status 401: El punto de acceso no pertenece a la empresa que tienes asignada