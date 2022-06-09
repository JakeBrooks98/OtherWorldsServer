from otherworldsapi.models import Region
from rest_framework import serializers

class RegionSerializer(serializers.ModelSerializer):
    """JSON serializer for Regions
    """
    class Meta:
        model = Region
        fields = ('id','description', 'name')
        depth = 2
        
class CreateRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'description', 'name']