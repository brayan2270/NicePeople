===========================================
 Recurso de Activacion de Usuario por Token
===========================================


Recurso PATCH
------------
.. http:post:: /api/v1/uuser/activate/<str:token>

Activa el usuario despues de llegar el token de activacion de usuario al correo


**Ejemplo de petición**

.. sourcecode:: http

    PATCH /api/v1/user/activate/7LWq6gOHYh9cciIpV2zRg5.... HTTP/1.1
    Content-Type: application/json


**Ejemplos de respuesta**

.. sourcecode:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "status code": 200,
        "message": "User activated successfully"
    }

.. sourcecode:: http

    HTTP/1.1 404 NOT_FOUND
    Content-Type: application/json

    {
        {
            "code": "token_not_found",
            "detailed": "Token no encontrado"
        }
    }

.. sourcecode:: http

    HTTP/1.1 202 ACCEPTED
    Content-Type: application/json

    {
        {
            "code": "token_expired_or_used",
            "detailed": "Token ya usado o vencido"
        }
    }


:status 200: User activated successfully
:status 202: Token ya usado o vencido
:status 404: Token no encontrado