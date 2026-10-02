from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def pierwszy_endpoint(request):
    return Response({
        "message": "Pierwszy endpoint działa!"
    })


