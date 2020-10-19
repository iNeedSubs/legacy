from rest_framework.views import exception_handler
from rest_framework import status


def get_exception(key: str) -> int:
    '''
    Key: ErrType
    Value: Status Code
    Return: Status Code
    '''
    EXCEPTIONS = {
        'NO_QUERY': 400,
        'INVALID_TYPE': 404,
        'INVALID_REQ_METHOD': 405,
        'NO_ID': 400,
        'NOT_FOUND': 404,
        'WRONG_LANG_CODE': 400,
        'WRONG_ID': 404,
        'WRONG_RETURN_TYPE': 400
    }
    return EXCEPTIONS[key]


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
