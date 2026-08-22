from django.urls import path, include

from . import views

app_name = "reservations"

htmx_urlpatterns = [
    path("temp/", views.query_bar, name="query_bar"),
]

urlpatterns = [
    path("htmx/", include(htmx_urlpatterns)),
]
