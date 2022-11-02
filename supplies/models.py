from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=250, null=True, blank=True)
    price = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField(max_length=250, null=True, blank=True)
    contact = models.CharField(max_length=280, null=True, blank=True)
    is_finished = models.BooleanField(default=False)


# # Create your models here.
# class Product(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#     title = models.CharField(max_length=250, null=True)
#     price = models.IntegerField()
#     description = models.CharField(max_length=140, null=True, blank=True)
#     # is_finished = models.BooleanField(default=False)
#     # title = models.CharField(max_length=250, null=True)
#     # price = models.FloatField()
#     # contact = models.CharField(max_length=250, null=True)
#     # #image
