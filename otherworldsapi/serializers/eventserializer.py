from otherworldsapi.models import Events
from rest_framework import serializers

from otherworldsapi.serializers.worldserializers import WorldSerializer

class EventsSerializer(serializers.ModelSerializer):
    """JSON serializer for Events
    """
    world=WorldSerializer()
    class Meta:
        model = Events
        fields = ('id','description', 'world', 'name', 'date', 'date_suffix')
        depth = 2
        
class CreateEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['id', 'description', 'name', 'date', 'date_suffix']