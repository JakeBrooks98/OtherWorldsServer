from django.db import models
from otherworldsapi.models.world import World


class Map(models.Model):
    map_image = models.TextField()
    world = models.ForeignKey(
        "World", on_delete=models.CASCADE, related_name='image')