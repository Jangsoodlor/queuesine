from django.views import generic
from .models import Restaurant


class RestaurantListView(generic.ListView):
    template_name = "restaurants/index.html"
    context_object_name = "restaurants"

    def get_queryset(self):
        restaurants = Restaurant.objects.all()
        return restaurants.order_by("name")


class RestaurantDetailView(generic.DetailView):
    model = Restaurant
    template_name = "restaurants/detail.html"
