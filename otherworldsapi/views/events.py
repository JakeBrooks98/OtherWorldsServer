from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from otherworldsapi.models.events import Events
from otherworldsapi.serializers.eventserializer import CreateEventsSerializer

class EventView(ViewSet):
    """Other Worlds event view"""
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized event instance
        """
        world = request.data['world']
        serializer = CreateEventsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(world = world)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, pk):
        event = Events.objects.get(pk=pk)
        event.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)