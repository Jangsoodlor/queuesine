from django.shortcuts import render, redirect
from datetime import date, timedelta

GUEST_CHOICES = {
    "1": "1 person",
    "2": "2 people",
    "3": "3 people",
    "4": "4 people",
    "5": "5 people",
    "6": "6 people",
    "7": "7+ people",
}


def query_bar(request, restaurant_id: int):
    context = {
        "restaurant_id": restaurant_id,
        "reservation_date": request.GET.get("reservation_date", ""),
        "reservation_time": request.GET.get("reservation_time", ""),
        "guest_choices": GUEST_CHOICES,
        "selected_party_size": "2",
    }
    return render(request, "reservations/htmx/query_bar.html", context)


def select_table(request, restaurant_id: int):
    """Receives POST request from query_bar form and renders table selection page.

    :param request: POST request.
    :param restaurant_id: id of the restaurant
    :raises ValueError: when request type is not POST
    """
    if not request.POST:
        return redirect("error.html")

    context = {
        "reservation_date": request.POST.get("reservation_date"),
        "reservation_time": request.POST.get("reservation_time"),
        "party_size": request.POST.get("party_size"),
    }

    return render(request, "reservations/select_table.html", context=context)


def table_reserved(request, restaurant_id: int):
    pass
