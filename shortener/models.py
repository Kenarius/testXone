from django.db import models
from django.contrib.auth.models import User


class Shorts(models.Model):
    fullurl = models.CharField(max_length=250)
    shorturl = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_data')
