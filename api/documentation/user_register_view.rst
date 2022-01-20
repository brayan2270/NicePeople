================================
 Recurso de Creacion de Usuarios
================================


Recurso POST
------------
.. http:post:: /api/v1/user/register

Autentica al usuario y Crea el usuario.

**Campos obligatorios**

:email: **(string)** Correo del usuario
:password: **(string)** Contraseña del Usuario
:first_name: **(string)** Primer Nombre
:last_name: **(string)** Segundo Nombre
:profile: **(string)** Perfil
:cellphone: **(string)** Telefono
:departamento: **(string)** Departamento
:ciudad: **(string)** Ciudad
:pais: **(string)** Pais
:address: **(string)** Direccion
:empresa: **(string)** pk de la empresa


**Ejemplo de campo profile**

los perfiles estaran creados con una base de datos de Postgres que se enviara adjunta en la prueba.

:1 = Administrador
:2 = Administrador de empresa
:3 = Empleado de empresa


**Ejemplo de petición**

.. sourcecode:: http

    POST /api/v1/user/register HTTP/1.1
    Content-Type: application/json

    {
        "email": "prueba@gmail.com",
        "password": "12345",
        "first_name": "prueba",
        "last_name": "prueba1",
        "profile": "2",
        "cellphone": "2343231314",
        "departamento": "Risaralda",
        "ciudad": "Pereira",
        "pais": "Colombia",
        "address": "prueba direccion"
        "empresa": 1
    }

**Ejemplos de respuesta**

.. sourcecode:: http

    HTTP/1.1 201 CREATED
    Content-Type: application/json

    {
        "status code": 201,
        "message": "successfully created company",
        "inserted": 20
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


:status 201: successfully created company
:status 400: Cuerpo de la petición con estructura inválida
:status 403: No tiene los permisos necesarios
:status 401: El token es incorrecto o expiro
