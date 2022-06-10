from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from otherworldsapi.models import World
from otherworldsapi.serializers.regionserializer import CreateRegionSerializer

class RegionView(ViewSet):
    """Other Worlds event view"""
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized event instance
        """
        world = World.objects.get(pk=request.data['world'])
        serializer = CreateRegionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(world = world)
        return Response(serializer.data, status=status.HTTP_201_CREATED)