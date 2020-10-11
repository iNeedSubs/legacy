from rest_framework.views import exception_handler
from rest_framework import status


def handle_405_exception(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    if response is not None:
        if response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED:
            payload = {
                'detail': 'Used wrong method to make the request',
                'type': 'INVALID_REQ_METHOD'
            }
            response.data = payload

    return response
