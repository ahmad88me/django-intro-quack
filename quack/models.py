from django.db import models


class Duck(models.Model):
    color = models.CharField(max_length=30, default='yellow')
    model = models.CharField(max_length=30)
    price = models.FloatField(default=0)

