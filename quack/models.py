from django.db import models
from django.contrib.auth.models import User


class Duck(models.Model):
    color = models.CharField(max_length=30, default='yellow')
    model = models.CharField(max_length=30)
    price = models.FloatField(default=0)
    owner = models.ForeignKey(User, null=True)


