### ¿Cómo usar?

#### Linux:

1. Clonar Proyecto
2. Crear entorno virtual `python3 -m venv .venv`
3. entrar al entrorno vitrual `source .venv/bin/activate`
4. Instalar dependencias `pip install -r requirements.txt`
5. importar copia de base de datos que es la cual tiene los 3 tipos de perfiles de usuarios creados.
   Tambien cuanta con usuario administrador creado.
6. Database : useitdatabase.
10. Iniciar servidor Django `python manage.py runserver`


#### Endpoints Auth:

1. `http://localhost:8000/auth`: 
```
{
    "username": "prueba@admin.com",
    "password": "12345"
}
```