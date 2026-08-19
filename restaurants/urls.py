from django.urls import path, include

from . import views

app_name = "restaurants"

htmx_urlpatterns = [
    path("<int:pk>/menus/", views.menu_listing, name="menu_listing"),
    path("restaurants/", views.restaurant_listing, name="restaurant_listing"),
]

urlpatterns = [
    path("", views.restaurant_index, name="restaurant_index"),
    path(
        "<int:pk>/",
        views.RestaurantDetailView.as_view(),
        name="restaurant_detail",
    ),
    path("partials/", include(htmx_urlpatterns)),
]
