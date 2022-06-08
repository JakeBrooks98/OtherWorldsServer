from django.db import models
from django.contrib.auth.models import User


class World(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='worlds')
    description = models.CharField(max_length=350)
    