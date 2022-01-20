=====================================================
 Recurso para Reenviar Token de Activacion de Usuario
=====================================================


Recurso PATCH
------------
.. http:post:: /api/v1/user/activate/email/<str:email>

Envia nuevo correo para activar un usuario


**Ejemplo de petición**

.. sourcecode:: http

    PATCH /api/v1/user/activate/email/prueba@gmail.com HTTP/1.1
    Content-Type: application/json


**Ejemplos de respuesta**

.. sourcecode:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "status code": 200,
        "message": "mail sent successfully"
    }

.. sourcecode:: http

    HTTP/1.1 400 BAD_REQUEST
    Content-Type: application/json

    {
        {
            "code": "user_activate",
            "detailed": "el usuario ya se encuentra activato"
        }
    }


:status 200: mail sent successfully
:status 400: el usuario ya se encuentra activato