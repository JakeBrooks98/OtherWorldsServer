from otherworldsapi.models import Biome
from rest_framework import serializers

class BiomeSerializer(serializers.ModelSerializer):
    """JSON serializer for biomes
    """
    class Meta:
        model = Biome
        fields = ('id','label')