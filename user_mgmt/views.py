from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def logout(request, version):
    # delete the token to force a login
    request.user.auth_token.delete()
    return Response({'success': True,
                     'details': {
                         'message': 'User logged out.'
                     }},
                    status=status.HTTP_200_OK)