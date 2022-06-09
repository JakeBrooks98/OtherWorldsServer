from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from otherworldsapi.models import World
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from otherworldsapi.models.events import Events
from otherworldsapi.models.region import Region
from otherworldsapi.serializers.worldserializers import WorldSerializer, CreateWorldSerializer
from rest_framework.decorators import action

class WorldView(ViewSet):
    """Other Worlds World view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single world 

        Returns:
            Response -- JSON serialized World 
        """
        world = World.objects.get(pk=pk)
        serializer = WorldSerializer(world)
        return Response(serializer.data)
        

    def list(self, request):
        """Handle GET requests to get all Worlds

        Returns:
            Response -- JSON serialized list of Worlds
        """
        worlds = World.objects.all()
        serializer = WorldSerializer(worlds, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized world instance
        """
        user = request.auth.user
        serializer = CreateWorldSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """Handle PUT requests for an world

        Returns:
            Response -- Empty body with 204 status code
        """
        world = World.objects.get(pk=pk)
        serializer = CreateWorldSerializer(world, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        world = World.objects.get(pk=pk)
        world.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)