from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=250, null=True)
    price = models.FloatField()
    contact = models.CharField(max_length=250, null=True)
    #image
