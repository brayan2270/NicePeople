==========================
 Recurso de Autenticación
==========================


Recurso POST
------------
.. http:post:: /api/v1/auth

Autentica al usuario y genera un token de acceso.

**Campos obligatorios**

:email: **(string)** Correo del usuario
:password: **(string)** Contraseña del Usuario

**Ejemplo de petición**

.. sourcecode:: http

    POST /api/v1/auth HTTP/1.1
    Content-Type: application/json

    {
        "username": "user@admin.com",
        "password": "12345"
    }

**Ejemplos de respuesta**

.. sourcecode:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "status code": 200,
        "message": "User logged in  successfully",
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9......."
    }

.. sourcecode:: http

    HTTP/1.1 403 FORBIDDEN
    Content-Type: application/json

    {
        {
            "code": "invalid_request",
            "detailed": "No se puede acceder porque su franja horaria caduco o la sede esta inactiva"
        }
    }

.. sourcecode:: http

    HTTP/1.1 400 BAD_REQUEST
    Content-Type: application/json

    {
        "code": "invalid_body",
        "detailed": "Cuerpo de la petición con estructura inválida",
        "data": {
            "non_field_errors": [
                "A user with this email and password is not found."
            ]
        }
    }


:status 200: User logged in  successfully
:status 400: A user with this email and password is not found
:status 403: No se puede acceder porque su franja horaria caduco o la sede esta inactiva