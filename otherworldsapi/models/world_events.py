from django.db import models

class WorldEvent(models.Model):
    world = models.ForeignKey("World", on_delete=models.CASCADE)
    event = models.ForeignKey("Events", on_delete=models.CASCADE)