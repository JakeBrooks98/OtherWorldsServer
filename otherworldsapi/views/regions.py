from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from otherworldsapi.models import World
from otherworldsapi.models.region import Region
from otherworldsapi.serializers.regionserializer import CreateRegionSerializer

class RegionView(ViewSet):
    """Other Worlds region view"""
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized region instance
        """
        world = World.objects.get(pk=request.data['world'])
        serializer = CreateRegionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(world = world)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, pk):
        region = Region.objects.get(pk=pk)
        region.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)