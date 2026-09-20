from datetime import date
from django.shortcuts import render
from .models import Table, TimeSlot
from django.contrib import messages


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
    """Renders the query bar

    The query bar let the user selects party size, date, and time
    to query table availability of a given restaurant. Once it is selected,
    it fires "newQuery" event and triggers table_selection method to reload the
    table selection section of the select_table page.

    :param request: Request (GET, POST)
    :param restaurant_id: Restaurant's ID
    :return: Render the query bar
    """
    time_slots = TimeSlot.objects.filter(restaurant=restaurant_id)
    context = {
        "restaurant_id": restaurant_id,
        "reservation_date": request.POST.get(
            "reservation_date", date.today().isoformat()
        ),
        "time_slots": time_slots,
        "guest_choices": GUEST_CHOICES,
        "selected_party_size": request.POST.get("party_size", "2"),
        "selected_time": request.POST.get("selected_time", ""),
    }
    response = render(request, "reservations/htmx/query_bar.html", context)
    response["HX-Trigger"] = "newQuery"
    return response


def table_selection(request, restaurant_id: int):
    reservation_date = request.GET.get("reservation_date", "")
    selected_party_size = request.GET.get("party_size", "2")
    selected_time = request.GET.get("selected_time", "")

    if not reservation_date or not selected_time:
        messages.error(request, "Please select both a date and time.")
        return render(request, "reservations/htmx/table_selection.html", {})

    available_tables = Table.objects.filter(
        restaurant=restaurant_id,
        capacity__gte=selected_party_size,
    ).exclude(
        reservation__time_slot=selected_time,
        reservation__date=reservation_date,
    )

    context = {"available_tables": available_tables}

    return render(request, "reservations/htmx/table_selection.html", context)


def select_table(request, restaurant_id: int):
    """Renders the select_table page.

    This page contains 2 HTMX elements: the query bar and the table selection.

    :param request: Request (GET)
    :param restaurant_id: Restaurant's ID
    :return: renders the select_table page.
    """
    context = {"restaurant_id": restaurant_id}

    return render(request, "reservations/select_table.html", context=context)
