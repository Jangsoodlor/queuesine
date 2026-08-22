from django.shortcuts import render, redirect
from django.http import HttpResponse


def query_bar(request):
    return render(request, "reservations/htmx/query_bar.html")


def find_vacant_tables(request, restaurant_id: int):
    """Receives POST request from query_bar form and

    :param request: POST request.
    :param restaurant_id: id of the restaurant
    :raises ValueError: when request type is not POST
    """
    if not request.POST:
        # TODO: create error page and redirect to that.
        raise ValueError("Must be post request")

    context = {
        "reservation_date": request.POST["reservation_date"],
        "reservation_time": request.POST["reservation_date"],
        "guests": request.POST["guests"],
    }

    # TODO: render show vacant table page (Don't redirect)
    return


def show_vacant_tables(request, restaurant_id: int):
    pass


def select_table(request, restaurant_id: int):
    pass


def table_reserved(request, restaurant_id: int):
    pass
