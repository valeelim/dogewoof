from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DogDescription(models.Model) :
    image = models.ImageField()
    name = models.CharField(max_length=100)
    first_description = models.TextField()
    secont_description = models.TextField()
    funfact = models.JSONField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)