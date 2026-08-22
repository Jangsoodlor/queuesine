from django.db import models


class Table(models.Model):
    name = models.CharField(max_length=255)
    capacity = models.IntegerField()
    restaurant = models.ForeignKey(
        "restaurants.Restaurant",
        on_delete=models.CASCADE,
        related_name="tables",
    )


class Reservation(models.Model):
    # TODO: link to customer
    table = models.ForeignKey(
        Table,
        on_delete=models.CASCADE,
        related_name="reservations",
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
