from otherworldsapi.models import World
from rest_framework import serializers

class WorldSerializer(serializers.ModelSerializer):
    """JSON serializer for worlds
    """
    class Meta:
        model = World
        fields = ('id','description', 'user', 'name', 'events','regions')
        depth = 2
        
class CreateWorldSerializer(serializers.ModelSerializer):
    class Meta:
        model = World
        fields = ['id', 'description', 'name', 'user']