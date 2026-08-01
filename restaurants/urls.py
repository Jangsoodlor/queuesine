from django.urls import path, include

from . import views

app_name = "restaurants"

htmx_urlpatterns = [
    path("<int:pk>/menus/", views.restaurant_menus, name="restaurant_menus"),
]

urlpatterns = [
    path("", views.RestaurantListView.as_view(), name="restaurant_index"),
    path(
        "<int:pk>/",
        views.RestaurantDetailView.as_view(),
        name="restaurant_detail",
    ),
    path("partials/", include(htmx_urlpatterns)),
]
