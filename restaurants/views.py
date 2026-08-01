from django.views import generic
from .models import Restaurant, Menu
from django.shortcuts import render


class RestaurantListView(generic.ListView):
    template_name = "restaurants/index.html"
    context_object_name = "restaurants"

    def get_queryset(self):
        restaurants = Restaurant.objects.all()
        return restaurants.order_by("name")


class RestaurantDetailView(generic.DetailView):
    model = Restaurant
    template_name = "restaurants/detail.html"


def restaurant_menus(request, pk: int):
    context = {"menus": Menu.objects.filter(restaurant_id=pk)}
    return render(request, "partials/menus.html", context)
