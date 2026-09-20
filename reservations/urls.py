from django.urls import path, include

from . import views

app_name = "reservations"

htmx_urlpatterns = [
    path("query_bar/<int:restaurant_id>", views.query_bar, name="query_bar"),
    path(
        "table_selection/<int:restaurant_id>",
        views.table_selection,
        name="table_selection",
    ),
]

urlpatterns = [
    path("reserve/<int:restaurant_id>/", views.select_table, name="select_table"),
    path("htmx/", include(htmx_urlpatterns)),
]
