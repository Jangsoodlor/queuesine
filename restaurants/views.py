from django.views import generic
from .models import Restaurant, Menu
from django.shortcuts import render


def restaurant_index(request):
    return render(request, "restaurants/index.html")


class RestaurantDetailView(generic.DetailView):
    model = Restaurant
    template_name = "restaurants/detail.html"


def menu_listing(request, pk: int):
    context = {"menus": Menu.objects.filter(restaurant_id=pk)}
    return render(request, "partials/menu_listing.html", context)


def restaurant_listing(request):
    context = {"restaurants": Restaurant.objects.all()}
    return render(request, "partials/restaurant_listing.html", context)
