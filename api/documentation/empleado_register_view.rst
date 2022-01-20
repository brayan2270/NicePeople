=========================================
 Recurso de Creacion de Usuarios Empleado
=========================================


Recurso POST
------------
.. http:post:: /api/v1/empleado/register/<int:pk>

Crea el usuario empleado y le asigna automatico la empresa del usuario el cual envio el correo.

**Campos obligatorios**

:email: **(string)** Correo del usuario
:password: **(string)** Contraseña del Usuario
:first_name: **(string)** Primer Nombre
:last_name: **(string)** Segundo Nombre
:cellphone: **(string)** Telefono
:departamento: **(string)** Departamento
:ciudad: **(string)** Ciudad
:pais: **(string)** Pais
:address: **(string)** Direccion


**Ejemplo de petición**

.. sourcecode:: http

    POST /api/v1/empleado/register/1 HTTP/1.1
    Content-Type: application/json

    {
        "email": "pruebaempleado@gmail.com",
        "password": "12345",
        "first_name": "prueba",
        "last_name": "prueba1",
        "cellphone": "2343231314",
        "departamento": "Risaralda",
        "ciudad": "Pereira",
        "pais": "Colombia",
        "address": "prueba direccion"
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

    HTTP/1.1 400 BAD_REQUEST
    Content-Type: application/json

    {
        "code": "invalid_body",
        "detailed": "Cuerpo de la petición con estructura inválida"
        }
    }


:status 201: successfully created company
:status 400: Cuerpo de la petición con estructura inválida
