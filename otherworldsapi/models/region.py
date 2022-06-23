from django.db import models
from otherworldsapi.models.world import World


class Region(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    world = models.ForeignKey(
        "World", on_delete=models.CASCADE, related_name='regions')
    biome = models.ManyToManyField( "Biome", related_name='region')