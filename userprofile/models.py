from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    husky = 'Husky'
    CHOICES = ((husky, 'Husky'),
              ('Bulldog', 'Bulldog'),
              ('German Shepherd', 'German Shepherd'),
              ('Poodles', 'Poodles'),
              ('Shih Tzu', 'Shih Tzu'),
              ('Pomeranians', 'Pomeranians'),
              ('Chihuahua', 'Chihuahua'),
              ('Chow Chow', 'Chow Chow'),)


    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='userprofile/images', null=True, default='static/images/default.jpg')
    bio = models.TextField(null=True)
    saldo = models.BigIntegerField(default=0)
    phone = models.CharField(max_length=20 ,null=True)
    address = models.TextField(null=True)
    dogtype = models.CharField(choices=CHOICES, max_length=15, default=husky)
