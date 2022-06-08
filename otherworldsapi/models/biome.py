from django.db import models


class Biome(models.Model):
    label = models.CharField(max_length=30)
