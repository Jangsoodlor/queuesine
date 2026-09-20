from django.db import models


class Table(models.Model):
    """Representing restaurant tables."""

    name = models.CharField(max_length=255)
    capacity = models.IntegerField()
    restaurant = models.ForeignKey(
        "restaurants.Restaurant",
        on_delete=models.CASCADE,
        related_name="tables",
    )


class TimeSlot(models.Model):
    """Available time slot for booking for each restaurant."""

    restaurant = models.ForeignKey(
        "restaurants.Restaurant",
        on_delete=models.CASCADE,
    )
    time_slot = models.TimeField()


class Reservation(models.Model):
    """Reservation details of a user."""

    table = models.ForeignKey(
        Table,
        on_delete=models.CASCADE,
    )
    time_slot = models.ForeignKey(
        TimeSlot,
        on_delete=models.CASCADE,
    )
    date = models.DateField()
    booker = models.EmailField()
    customer_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
