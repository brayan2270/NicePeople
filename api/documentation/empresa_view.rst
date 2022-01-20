==========================
 Recurso de Creacion de Empresa
==========================


Recurso POST
------------
.. http:post:: /api/v1/empresa/register

Autentica al usuario y Crea la empresa.

**Campos obligatorios**

:nit: **(string)** Nit de la empresa
:nombre_empresa: **(string)** Nombre de la empresa
:nombre_comercial_empresa: **(string)** Nombre comercial de la empresa
:direccion: **(string)** Direccion de la empresa
:telephone: **(string)** Telefino de la empresa
:email: **(string, con validador de email)** Correo electronico de la emrpresa
:sitio_web: **(string, con validador de url)** Sitio web de la empresa
:ciudad: **(string)** Ciudad de la empresa
:pais: **(string)** Pais de la empresa
:departamento: **(string)** Departamento de la empresa


**Ejemplo de petición**

.. sourcecode:: http

    POST /api/v1/empresa/register HTTP/1.1
    Content-Type: application/json

    {
        "nit": "11111",
        "nombre_empresa": "prueba empresa",
        "nombre_comercial_empresa": "prueba empresa comercial",
        "direccion": "sssss",
        "telephone": "1231231",
        "email": "pruebaempresa@gmail.com",
        "sitio_web": "https://www.google.com/",
        "ciudad": "Pereira",
        "pais": "Colombia",
        "departamento": "Risaralda"

    }

**Ejemplos de respuesta**

.. sourcecode:: http

    HTTP/1.1 201 CREATED
    Content-Type: application/json

    {
        "status code": 201,
        "message": "User created successfully",
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


:status 201: User logged in  successfully
:status 400: Cuerpo de la petición con estructura inválida
:status 403: No tiene los permisos necesarios
:status 401: El token es incorrecto o expiro