from django.db import models
from django.contrib.auth.models import User
import datetime

class ContactUs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(blank=False, default=datetime.datetime.now().strftime(('%Y-%m-%d')))
    subject = models.CharField(max_length=255)
    description = models.TextField()