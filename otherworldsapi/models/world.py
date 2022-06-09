from django.db import models
from django.contrib.auth.models import User


class World(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='worlds')
    description = models.CharField(max_length=350)
    @property
    def is_user(self):
        return self.__is_user
    
    @is_user.setter
    def is_user(self,value):
        self.is_user=value