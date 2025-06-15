from rest_framework.response import Response

def standard_response(data=None, status_code=200, message="", error=None):
    return Response({
        "status_code": status_code,
        "message": message,
        "error": error,
        "data": data
    }, status=status_code)