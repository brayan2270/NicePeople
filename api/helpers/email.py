""" Defines email sending helper """

import re
import os

from django.core.mail import EmailMessage
from django.conf import settings
from rest_framework import status
from cerberus import Validator

from django.conf import settings

def email_service(data):
    """Email sending helper

    Parameters:
        data (dict):Contains email information.

    Returns:
        Response (message,status):A message and a status code

    """
    validator = Validator({
        "subject": {"required": True, "type": "string"},
        "body": {"required": True, "type": "string"},
        "email": {
            "required": True,
            "type": ["string", "list"],
            "schema": {
                "type": "string",
                "required": True,
                "regex": r'^[^@]+@[^@]+\.[^@]+'
            }
        }
    })

    if not validator.validate(data):
        return {
            "code": "invalid_email_format",
            "detailed": "Cuerpo de la petición con formato inválido",
            "data": validator.errors
        }, status.HTTP_400_BAD_REQUEST

    emails = []
    if isinstance(data.get('email'), str):
        emails.append(data.get('email'))
    elif isinstance(data.get('email'), list):
        emails.extend(data.get('email'))
    try:
        msg = EmailMessage(
            data.get("subject"),
            format(
                data.get("body")),
            settings.EMAIL_HOST_USER,
            emails)

        msg.content_subtype = "html"
        msg.send()

        return {}, status.HTTP_200_OK
    except:
        return {}, status.HTTP_502_BAD_GATEWAY
