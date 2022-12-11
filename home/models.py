from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class ContactUs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(blank=False, default=datetime.now)
    subject = models.CharField(max_length=255)
    description = models.TextField()

class Donation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()