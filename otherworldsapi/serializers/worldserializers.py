from otherworldsapi.models import World
from rest_framework import serializers

from otherworldsapi.serializers.eventserializer import EventsSerializer
from otherworldsapi.serializers.mapserializer import MapSerializer
from otherworldsapi.serializers.regionserializer import RegionSerializer

class WorldSerializer(serializers.ModelSerializer):
    """JSON serializer for worlds
    """
    events=EventsSerializer(many=True)
    regions=RegionSerializer(many=True)
    class Meta:
        model = World
        fields = ('id','description', 'name', 'events','regions', 'image', 'is_user')
        depth = 3
        
class CreateWorldSerializer(serializers.ModelSerializer):
    class Meta:
        model = World
        fields = ['id', 'description', 'name']