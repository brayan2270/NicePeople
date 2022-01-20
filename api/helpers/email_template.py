def get_email_user(first_name, last_name, email, password):
    """ Returns the message when an order was payed succesfully by buyer.

    Parameters
    ----------

    order_id: int
        Order id

    Return
    ------

    str: HTML message with message 

    """
    return (
        """

            <h1 style="text-align: center; padding-bottom: 20px;">
                ¡Creacion de usuario!
            </h1>
            <p>
                Hola, <b>{} {}</b>, 
                hemos creado un usuario administrador de empresa con los siguientes datos: <br><br>
                <b>username</b>: {}<br>
                <b>password</b>: {}<br><br>

                porfavor no compartir los datos con ninguna persona
            </p><br>
            <div style="text-align: center; padding-bottom: 10px">
                <a style="
                            background-color: #4174fb;
                            border: none;
                            color: white;
                            padding: 15px 32px;
                            text-align: center;
                            text-decoration: none;
                            display: inline-block;
                            font-size: 16px;
                            margin: 4px 2px;
                            cursor: pointer;
                            border-radius: 10px;"
                        href="http://127.0.0.1:8000/api/v1/auth">
                    Ir al Login</a>
            </div>
        """
    ).format(first_name, last_name, email, password)



def get_email_employee(nombre_empresa, empresa):
    """ Returns the message when an order was payed succesfully by buyer.

    Parameters
    ----------

    order_id: int
        Order id

    Return
    ------

    str: HTML message with message 

    """
    return (
        """

            <h1 style="text-align: center; padding-bottom: 20px;">
                ¡Creacion de usuario!
            </h1>
            <p>
                Hola, 
                Te enviamos este correo para que te puedas registrar como <br>
                empleado de nuestra empresa {}
            </p><br>
            <div style="text-align: center; padding-bottom: 10px">
                <a style="
                            background-color: #4174fb;
                            border: none;
                            color: white;
                            padding: 15px 32px;
                            text-align: center;
                            text-decoration: none;
                            display: inline-block;
                            font-size: 16px;
                            margin: 4px 2px;
                            cursor: pointer;
                            border-radius: 10px;"
                        href="http://127.0.0.1:8000/api/v1/empleado/register/{}">
                    Ir al Login</a>
            </div>
        """
    ).format(nombre_empresa, empresa)



def get_session(first_name, last_name, email, first_name2, last_name2):
    """ Returns the message when an order was payed succesfully by buyer.

    Parameters
    ----------

    order_id: int
        Order id

    Return
    ------

    str: HTML message with message 

    """
    return (
        """

            <h1 style="text-align: center; padding-bottom: 20px;">
                ¡Inicio de ingreso fallido!
            </h1>
            <p>
                Hola, <b>{} {}</b>, 
                hemos detectado un intento de ingreso fallido de la siguiente persona: <br><br>
                <b>email</b>: {}<br>
                <b>nombre</b>: {} {}
            </p>
            </div>
        """
    ).format(first_name, last_name, email, first_name2, last_name2)



def get_Activate_user(first_name, last_name, token):
    """ Returns the message when an order was payed succesfully by buyer.

    Parameters
    ----------

    order_id: int
        Order id

    Return
    ------

    str: HTML message with message 

    """
    return (
        """

            <h1 style="text-align: center; padding-bottom: 20px;">
                ¡Activacion de Usuario!
            </h1>
            <p>
                Hola, <b>{} {}</b>, 
                hemos creado tu usuario, para poderlo activar da click en el siguiente boton: <br>
            </p><br>
            <div style="text-align: center; padding-bottom: 10px">
                <a style="
                            background-color: #4174fb;
                            border: none;
                            color: white;
                            padding: 15px 32px;
                            text-align: center;
                            text-decoration: none;
                            display: inline-block;
                            font-size: 16px;
                            margin: 4px 2px;
                            cursor: pointer;
                            border-radius: 10px;"
                        href="http://127.0.0.1:8000/api/v1/user/activate/{}">
                    Activar</a>
            </div>
        """
    ).format(first_name, last_name, token)