from otherworldsapi.models import World
from rest_framework import serializers

class WorldSerializer(serializers.ModelSerializer):
    """JSON serializer for worlds
    """
    class Meta:
        model = World
        fields = ('id','description', 'user', 'name', 'events','regions', 'is_user')
        depth = 3
        
class CreateWorldSerializer(serializers.ModelSerializer):
    class Meta:
        model = World
        fields = ['id', 'description', 'name']