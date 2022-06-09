from otherworldsapi.models import Events
from rest_framework import serializers

class EventsSerializer(serializers.ModelSerializer):
    """JSON serializer for Events
    """
    class Meta:
        model = Events
        fields = ('id','description', 'name')
        depth = 2
        
class CreateEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['id', 'description', 'name']