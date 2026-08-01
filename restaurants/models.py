from django.db import models
# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, blank=True, null=True)
    address = models.CharField(max_length=1000)
    latitude = models.FloatField()
    longitude = models.FloatField()
    image = models.URLField(blank=True, null=True)
    city = models.CharField(max_length=255)


class Menu(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, blank=True, null=True)
    price = models.FloatField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    category = models.CharField(max_length=255)
    image = models.URLField(blank=True, null=True)
