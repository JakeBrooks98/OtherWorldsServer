from otherworldsapi.models import Map
from rest_framework import serializers

class MapSerializer(serializers.ModelSerializer):
    """JSON serializer for Map
    """
    class Meta:
        model = Map
        fields = ('id','map', 'world')
        depth = 2
        
class CreateMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = ['id', 'map']