from django.db import models
from otherworldsapi.models.world import World



class Events(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=350)
    world = models.ManyToManyField("World", related_name='events')
    date = models.IntegerField()
    date_suffix = models.CharField(max_length=6)
    
    class Meta: 
        ordering=['date']