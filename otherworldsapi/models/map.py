from django.db import models
from otherworldsapi.models.world import World


class Map(models.Model):
    map = models.CharField(max_length=200)
    world = models.ForeignKey(
        "World", on_delete=models.CASCADE, related_name='image')