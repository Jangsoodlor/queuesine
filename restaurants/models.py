from django.db import models
# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, blank=True)
    address = models.CharField(max_length=1000)
    latitude = models.FloatField()
    longitude = models.FloatField()
    image = models.URLField(blank=True)


class Menu(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.FloatField()
    restaurant = models.ForeignKey("restaurants.restaurant")
    category = models.CharField(max_length=255)
