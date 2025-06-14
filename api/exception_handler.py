from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    response = drf_exception_handler(exc, context)

    if response is not None:
        error_message = ""

        if isinstance(exc, ValidationError):
            # Get string error message
            error_message = str(exc.detail[0]) if isinstance(exc.detail, list) else str(exc.detail)
        else:
            error_message = str(exc)

        response.data = {
            "status_code": response.status_code,
            "error_message": error_message,
            "error": response.data
        }

    return response
