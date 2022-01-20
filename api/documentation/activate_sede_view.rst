=====================================================
 Recurso para Activar y Descativar Sede
=====================================================


Recurso PATCH
------------
.. http:post:: /api/v1/activate/sede/<int:pk>

Activa y desactiva sede

**Campos obligatorios**

:estado: **(boolean)** estado de la sede

**Ejemplo de petición**

.. sourcecode:: http

    PATCH /api/v1/activate/sede/1 HTTP/1.1
    Content-Type: application/json

    {
        "estado": false
    }


**Ejemplos de respuesta**

.. sourcecode:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
    "status code": 200,
    "message": "headquarters status updated",
    "sede": false
}

.. sourcecode:: http

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

:status 200: headquarters status updated
:status 400: Cuerpo de la petición con estructura inválida
:status 403: No tiene los permisos necesarios
:status 401: El token es incorrecto o expiro