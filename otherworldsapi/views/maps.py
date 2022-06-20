from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from otherworldsapi.models.map import Map
from otherworldsapi.models import World
from otherworldsapi.serializers import CreateMapSerializer

class MapView(ViewSet):
    """Other Worlds map view"""
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized map instance
        """
        world = World.objects.get(pk=request.data['world'])
        serializer = CreateMapSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(world = world)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, pk):
        map = Map.objects.get(pk=pk)
        map.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)