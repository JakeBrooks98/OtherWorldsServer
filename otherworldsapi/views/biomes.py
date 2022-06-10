from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from otherworldsapi.models.biome import Biome
from otherworldsapi.serializers.biomeserializer import BiomeSerializer


class BiomeView(ViewSet):
    """Other Worlds biome view"""
    
    def list(self, request):
        """Handle GET requests to get all biomes

        Returns:
            Response -- JSON serialized list of biomes
        """
        biomes = Biome.objects.all()
        serializer = BiomeSerializer(biomes, many=True)
        return Response(serializer.data)