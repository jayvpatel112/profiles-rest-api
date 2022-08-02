from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Helloserializer
from rest_framework import status
from rest_framework import viewsets

# Create your views here.

@api_view(['GET'])
def helloapi(request):
    an_apiview = [
        'It is similar to Django view',
        'It mapped mutually to URLS',
        'It gives most control over application Logic'
    ]
    return Response({"status":200, "an_apiview": an_apiview})

@api_view(['POST'])
def posthelloapi(request):
    data = request.data
    serializer = Helloserializer(data=request.data)
    if serializer.is_valid():
        return Response({"message": serializer.data})
    return Response(
        serializer.errors,
        status = status.HTTP_400_BAD_REQUEST
    )

@api_view(['PATCH'])
def updateapi(request):
    data = request.data
    serializer = Helloserializer(data=request.data, partial=True)
    if serializer.is_valid():
        return Response({'message': serializer.data})
    return Response(
        serializer.errors,
        status = status.HTTP_400_BAD_REQUEST
    )

class Helloviewset(viewsets.ViewSet):
    """test api viewsets"""
    # serializer_class = Helloserializer
    def list(self, request):
        """return a hello message"""
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partialupdate)',
            'Automatically maps to urls using Routers',
            'Provides more functionality with less code'
        ]
        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """create a new hello message"""
        serializer = Helloserializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}!"
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )
    def retrieve(self, request, pk=None):
        """Handle getting an object by its id"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method': 'Delete'})