from django.db import models
from django.contrib.auth.models import *

class DogItem(models.Model):
    item_title = models.CharField(max_length=32)
    price = models.IntegerField()
    breed = models.CharField(max_length=16)
    description = models.TextField()
    image = models.ImageField()
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)